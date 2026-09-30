# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [unreleased]


## [1.1.0-rc.8] - 2026-09-30

### Changed
* `proposed_cluster_ids` description: used for curator placement recommendations; no follow-up request after an ERS timeout
* `error_type` description: example broadened to the exception name or its fully qualified name
* Gherkin features and sequence diagrams aligned with the ERS–ERE message vocabulary and delivery semantics


## [1.1.0-rc.6] - 2026-07-16

### Removed
* Contractor-specific references removed from the source code repositories (TEDSWS-528)


## [1.0.0-rc.2] - 2026-06-30

### Changed
* Minor documentation improvements (TEDSWS-520)
* Contractor-specific references removed from the source code repositories (TEDSWS-528)


## [1.0.0-rc.1] - 2026-04-21
### Added
* data model: `context` field on `EntityMention` — carries the surrounding textual context for an entity mention

### Changed
* Repository layout restructured: schemas, scripts, templates, and build configuration consolidated under `src/`; root-level `resources/`, `Makefile`, `pyproject.toml` and `poetry.lock` moved into `src/`
* Schema files renamed to drop the version suffix (e.g. `core-schema-v0.1.0.yaml` → `core-schema.yaml`); internal schema version bumped to 1.0.0
* Makefile: build logic consolidated into a single root-level `Makefile`; CI workflows updated to match revised `make` targets and paths
* Gherkin test suite overhauled: new feature files added for outcome integration, request publishing, and detailed resolution cases; outdated `ere-ers-common-cases` and `ere-ers-full-rebuilds` feature files removed; unhappy-path scenarios significantly extended
* Schema docs and worked examples updated to reflect the current schema structure and revised repository paths

### Fixed
* CI: PR comment step is now skipped on cross-fork pull requests to prevent permission failures

## [0.2.0-rc.2] - 2026-02-20
### Added
* CI: GitHub Actions quality-check workflow (`.github/workflows/code-quality.yaml`) — LinkML schema linting, `ruff` Python linting, model/docs generation with sync verification, and PR comment posting ([ERS1-103])
* `lint` and `lint-schema` Make targets ([ERS1-103])
* data model: `proposed_cluster_ids` field on `EntityMentionResolutionRequest` — allows the caller to suggest candidate clusters; the ERE has no obligation to honour the proposal ([ERS1-119])
* data model: `similarity_score` field on `ClusterReference` — a 0–1 pairwise score between an entity mention and a cluster representative ([ERS1-119])
* Schema docs: `EREErrorResponse.md`, `EREMessage.md`, `EntityMentionResolutionResponse.md`, `proposed_cluster_ids.md`, `similarity_score.md` ([ERS1-119])

### Changed
* data model: revised semantics of `excluded_cluster_ids` — ERE has no obligation to honour exclusions, and it remains the ultimate resolution authority ([ERS1-119])
* data model: clarified `ere_request_id` — notification responses originating inside the ERE (without a prior request) use the prefix `ereNotification:` ([ERS1-119])
* Removed `FullRebuildRequest` / `FullRebuildResponse` classes from ERE schema and docs ([ERS1-119])
* Renamed `entityType.md` → `EntityType.md` in schema docs ([ERS1-119])
* Gherkin tests updated to reflect the V4 ERE Contract — simplified idempotent-resolution scenarios, added full-rebuild stub, aligned unhappy-path tests ([ERS1-120])
* README updated: added `lint` / `lint-schema` targets to the Makefile overview ([ERS1-103])

## [0.2.0-rc.1] - 2026-02-03
### Added
* Architecture diagram PNGs under `docs/architecture/diagrams/`
* Mermaid sequence diagrams under `docs/architecture/sequence_diagrams/`

### Changed
* data model changed according to recent
  * Terminology cleaned (eg, "cluster reference" in place of "alignment option")
	* Simplifications (eg, alignment set removed)
	* Entity mention ID based on `requestID` + `sourceID` + `entityType`
* Documentation updates, eg, sequence diagram
* Gherkin tests updated according to the cases described in the new ERE Technical Contract
* README updated: added Documentation Overview with links to schema docs (`docs/schema/README.md`), architecture diagrams (`docs/architecture/diagrams/`), Mermaid sequences (`docs/architecture/sequence_diagrams/`), and an informative ERS–ERE interface note (`docs/ere-interface-seq-diag.md`)


## [0.1.0-rc.2] - 2026-01-16
### Added
* data model: Support for rejected canonical identifiers
* data model: Support for a full rebuild

### Changed
* Updated and refined data model
* Updated ERS-ERE  examples


## [0.1.0-rc.1] - 2025-12-22

* Initial release, fulfilling Project's Delivery 1 (ERE Technical Contract and related code).
* [LinkML schema](src/resources/schemas/core-schema.yaml) to specify the interaction with the ERE service.
	* Includes auto-generated [navigable documents](docs/schema/README.md), a [class diagram](docs/schema/README.md) and a [sequence diagram](docs/ere-interface-seq-diag.png).
* [Gherkin Tests](test/features/), based on [collected test data](test/test_data/), possible [test cases](test/test_data/analysis/README.md)
