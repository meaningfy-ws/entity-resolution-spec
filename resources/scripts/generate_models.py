import os
from pathlib import Path

from linkml.generators.pydanticgen import PydanticGenerator
from linkml.generators.pydanticgen.pydanticgen import SplitMode


PROJECT_ROOT = Path(__file__).parent.parent.parent.resolve()
SCHEMAS_DIR = PROJECT_ROOT / "resources" / "schemas"
TEMPLATE_DIR = PROJECT_ROOT / "resources" / "templates"
MODELS_DIR = PROJECT_ROOT / "src" / "ere" / "models"

# TODO: get these constants as args from cli when called from makefile
ERE_SCHEMA = SCHEMAS_DIR / "ere-service-schema-v0.1.0.yaml"


def generate_models() -> None:
    """Generate all models from curation schema using split generation."""
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Change to schemas directory so relative imports work
    original_dir = Path.cwd()
    os.chdir(SCHEMAS_DIR)
    
    try:
        results = PydanticGenerator.generate_split(
            schema=str(ERE_SCHEMA.name),
            output_path=str(MODELS_DIR / "ere.py"),
            split_pattern=".{{ schema.name | replace('Schema', '') | replace('-', '_') | lower }}",
            template_dir=str(TEMPLATE_DIR),
            split_mode=SplitMode.FULL,
        )

        print(f"Generated {len(results)} modules.")
    finally:
        os.chdir(original_dir)


if __name__ == "__main__":
    generate_models()
