# Entity Resolution Specifications

[![PyPI version](https://img.shields.io/pypi/v/ers-core.svg)](https://pypi.org/project/ers-core/)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=OP-TED_entity-resolution-spec&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=OP-TED_entity-resolution-spec)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=OP-TED_entity-resolution-spec&metric=bugs)](https://sonarcloud.io/summary/new_code?id=OP-TED_entity-resolution-spec)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=OP-TED_entity-resolution-spec&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=OP-TED_entity-resolution-spec)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=OP-TED_entity-resolution-spec&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=OP-TED_entity-resolution-spec)

Formal software contract, shared data models, sample messages, and compliance tests required for integrating new Entity Resolution Engines (EREs) into the system.

> Note: Active development continues in the OP-TED repository: https://github.com/OP-TED/entity-resolution-spec

## Requirements

- UNIX-compatible environment (Linux/macOS/WSL2)
- Make
- Python (managed via [uv](https://docs.astral.sh/uv/getting-started/installation/))

## Quick Start

```bash
make             # installs user dependencies via uv
make install-dev # installs development tooling (tests, lint, codegen)
make generate_models
make generate_docs
```

## Make targets overview

- `install`: install dependencies via Poetry
- `all`: generate all models, schemas, and documentation
- `generate-models`: regenerate Pydantic models and JSON Schema from LinkML
- `generate-doc`: regenerate documentation
- `lint`: run Pylint checks
- `lint-report`: generate Pylint report (for CI)
- `test`: run tests with coverage (no tests yet)
- `clean`: remove all generated artifacts

## Installation

To get started, you need a UNIX-compatible environment (Mac/Linux/WSL2) with Make, Python and [Poetry](https://python-poetry.org/). You can then use the following command to setup your environment:

```bash
make install
```

This will install the necessary user dependencies in a Poetry-managed virtual environment.


## Development

This project uses principles of model-driven development (MDD) and domain-driven design (DDD). The core model is defined in the `resources/linkml` directory, and the Python (Pydantic) models (pluralized to refer to all the classes as is the practice in the programming community) are generated using the [LinkML](https://linkml.io/) framework.

Generated Python models are in `src/models`. Regenerate them with:
The generated Python models can be found in the `src/models` directory. 
You can regenerate both the LinkML-based models (Python, JSONSchema) and the navigable documentation, by running:

```bash
make all
```

*the Makefile has more granular targets, see its content for details*.


## Running and Testing

TODO: this will be added in future. Right now, this repository contains
specifications only and does not have runnable unit tests.


## Test data

### Deduplicated notices

This repository contains manual deduplication for organizations and procedures from RDF tender notices. The duplication was done using fuzzy string matching with manual checking of the results.

[Details here](./test/test_data/README.md)

## Documentation Overview

Documentation resources for understanding the model, architecture, and interfaces:

### Model Schema Docs
See [docs/schema/README.md](docs/schema/README.md) — canonical data model and service schema documentation generated from the ERS–ERE definitions.

### Architectural Diagrams
See [docs/architecture/diagrams/README.md](docs/architecture/diagrams/README.md) — prescribed architectural diagrams illustrating system structure and components.

### Sequence Diagrams (Mermaid)
See [docs/architecture/sequence_diagrams/README.md](docs/architecture/sequence_diagrams/README.md) — Mermaid-format sequence diagrams describing key system interactions.

### Informative Interface Sequence
See [docs/ere-interface-seq-diag.md](docs/ere-interface-seq-diag.md) — informative sequence overview for ERS–ERE interactions.
Note: the ERS–ERE contract is the normative specification; this file is provided for additional context.

