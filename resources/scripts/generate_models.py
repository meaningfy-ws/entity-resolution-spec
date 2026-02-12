"""Generate Pydantic models from LinkML schemas using split generation.

This script is invoked by the Makefile and receives all paths as CLI arguments
so that the Makefile remains the single source of truth for project layout.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from linkml.generators.pydanticgen import PydanticGenerator
from linkml.generators.pydanticgen.pydanticgen import SplitMode

# Pattern applied to imported schema names to derive Python module names.
# e.g. "coreSchema" -> ".core"
SPLIT_PATTERN = ".{{ schema.name | replace('Schema', '') | replace('-', '_') | lower }}"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate Pydantic models from a LinkML schema.",
    )
    parser.add_argument(
        "--schema",
        required=True,
        type=Path,
        help="Path to the top-level LinkML YAML schema (e.g. resources/schemas/ere-service-schema-v0.1.0.yaml).",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Destination path for the main generated Python module (e.g. src/erspec/models/ere.py).",
    )
    parser.add_argument(
        "--template-dir",
        required=True,
        type=Path,
        help="Directory containing Jinja2 template overrides for the Pydantic generator.",
    )
    parser.add_argument(
        "--schemas-dir",
        required=True,
        type=Path,
        help="Directory that contains all schema YAML files (used as working directory for relative imports).",
    )
    return parser.parse_args(argv)


def generate_models(
    schema: Path,
    output: Path,
    template_dir: Path,
    schemas_dir: Path,
) -> None:
    """Generate all models from the given schema using split generation."""
    output.parent.mkdir(parents=True, exist_ok=True)

    # LinkML resolves relative schema imports from the CWD, so we need to
    # chdir into the schemas directory while generating.
    original_dir = Path.cwd()
    os.chdir(schemas_dir)

    try:
        results = PydanticGenerator.generate_split(
            schema=str(schema.name),
            output_path=str(output),
            split_pattern=SPLIT_PATTERN,
            template_dir=str(template_dir),
            split_mode=SplitMode.FULL,
        )
        print(f"Generated {len(results)} module(s).")
    finally:
        os.chdir(original_dir)


def main() -> None:
    args = parse_args()

    # Resolve all paths relative to the project root (CWD when Make invokes us).
    project_root = Path.cwd()
    schema = (project_root / args.schema).resolve()
    output = (project_root / args.output).resolve()
    template_dir = (project_root / args.template_dir).resolve()
    schemas_dir = (project_root / args.schemas_dir).resolve()

    for label, path in [("schema", schema), ("template-dir", template_dir), ("schemas-dir", schemas_dir)]:
        if not path.exists():
            print(f"Error: --{label} path does not exist: {path}", file=sys.stderr)
            sys.exit(1)

    generate_models(
        schema=schema,
        output=output,
        template_dir=template_dir,
        schemas_dir=schemas_dir,
    )


if __name__ == "__main__":
    main()
