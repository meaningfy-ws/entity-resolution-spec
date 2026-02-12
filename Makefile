SHELL=/bin/bash -o pipefail

# ─── Formatting ──────────────────────────────────────────────────────────────────

BUILD_PRINT  = \e[1;34m
END_PRINT    = \e[0m

ICON_DONE     = $(BUILD_PRINT)$(END_PRINT) [✔]
ICON_ERROR    = $(BUILD_PRINT)$(END_PRINT) [✗]
ICON_PROGRESS = $(BUILD_PRINT)$(END_PRINT) [-]

define log_progress
	@printf "$(ICON_PROGRESS) $(BUILD_PRINT)$(1)$(END_PRINT)\n"
endef

define log_done
	@printf "$(ICON_DONE) $(BUILD_PRINT)$(1)$(END_PRINT)\n"
endef

# ─── Paths & Naming ─────────────────────────────────────────────────────────────

SCHEMAS_DIR    = resources/schemas
SCRIPTS_DIR    = resources/scripts
TEMPLATES_DIR  = resources/templates
MODELS_DIR     = src/erspec/models

# Schema identifiers
ERE_SCHEMA_NAME    = ere-service-schema
CORE_SCHEMA_NAME   = core-schema
SCHEMA_VERSION     = 0.1.0

# Source schemas (core is imported by ere, so it is a dependency)
ERE_SCHEMA_PATH    = $(SCHEMAS_DIR)/$(ERE_SCHEMA_NAME)-v$(SCHEMA_VERSION).yaml
CORE_SCHEMA_PATH   = $(SCHEMAS_DIR)/$(CORE_SCHEMA_NAME)-v$(SCHEMA_VERSION).yaml
ALL_SCHEMA_SOURCES = $(ERE_SCHEMA_PATH) $(CORE_SCHEMA_PATH)

# Generated artefacts
PYTHON_ERE_MODEL   = $(MODELS_DIR)/ere.py
PYTHON_CORE_MODEL  = $(MODELS_DIR)/core.py
JSON_SCHEMA_PATH   = $(SCHEMAS_DIR)/$(ERE_SCHEMA_NAME)-v$(SCHEMA_VERSION).json

MODEL_DOCS_DIR     = docs/schema
MODEL_DOCS_README  = $(MODEL_DOCS_DIR)/README.md

# ─── Help ────────────────────────────────────────────────────────────────────────

.PHONY: help
help:
	@echo ""
	@echo "Usage:"
	@echo "  make <target>"
	@echo ""
	@echo "Available targets:"
	@awk 'BEGIN {FS = ":.*##"; printf ""} \
		/^[a-zA-Z0-9_-]+:.*##/ { \
			printf "  \033[1;34m%-20s\033[0m %s\n", $$1, $$2 \
		}' $(MAKEFILE_LIST)

# ─── Setup ───────────────────────────────────────────────────────────────────────
# Note: Python, Poetry and Make are pre-requisites and are not handled here.

.PHONY: install
install: ## Install dependencies using Poetry
	$(call log_progress,Installing dependencies using Poetry...)
	@poetry sync
	$(call log_done,Dependencies installed.)

# ─── Aggregate targets ──────────────────────────────────────────────────────────

.PHONY: all
all: generate-models generate-doc ## Generate all artefacts (models + docs)
	$(call log_done,All artefacts generated.)

.PHONY: generate-models
generate-models: $(PYTHON_ERE_MODEL) $(JSON_SCHEMA_PATH) ## Generate Python models and JSON Schema
	$(call log_done,All models generated.)

.PHONY: generate-doc
generate-doc: $(MODEL_DOCS_README) ## Generate schema documentation and diagrams
	$(call log_done,Documentation generated.)

# ─── Python Pydantic models (split generation: ere + core) ──────────────────────

$(PYTHON_ERE_MODEL) $(PYTHON_CORE_MODEL) &: $(ALL_SCHEMA_SOURCES)
	$(call log_progress,Generating Python models...)
	@mkdir -p $(MODELS_DIR)
	@poetry run python $(SCRIPTS_DIR)/generate_models.py \
		--schema $(ERE_SCHEMA_PATH) \
		--output $(PYTHON_ERE_MODEL) \
		--template-dir $(TEMPLATES_DIR) \
		--schemas-dir $(SCHEMAS_DIR)
	@poetry run ruff check --fix $(MODELS_DIR)
	$(call log_done,Python models generated.)

# ─── JSON Schema ─────────────────────────────────────────────────────────────────
# The ERE schema imports core, so `linkml generate json-schema` will include both.

$(JSON_SCHEMA_PATH): $(ALL_SCHEMA_SOURCES)
	$(call log_progress,Generating JSON Schema...)
	@mkdir -p $(dir $(JSON_SCHEMA_PATH))
	@poetry run linkml generate json-schema --indent 2 $(ERE_SCHEMA_PATH) > $(JSON_SCHEMA_PATH)
	$(call log_done,JSON Schema generated -> $(JSON_SCHEMA_PATH))

# ─── Documentation & PlantUML diagrams ──────────────────────────────────────────

$(MODEL_DOCS_README): $(ALL_SCHEMA_SOURCES)
	$(call log_progress,Generating schema documentation...)
	@mkdir -p $(MODEL_DOCS_DIR)
# Index is named README.md so GitHub renders it when browsing the directory.
	@poetry run linkml generate doc $(ERE_SCHEMA_PATH) \
		-d $(MODEL_DOCS_DIR) --index-name README
# TODO: Prefer PNG once upstream is fixed (https://github.com/linkml/linkml/issues/3009)
	@poetry run linkml generate plantuml \
		-d $(MODEL_DOCS_DIR) --format svg $(ERE_SCHEMA_PATH)
	$(call log_done,Documentation generated -> $(MODEL_DOCS_DIR))

# ─── Clean ───────────────────────────────────────────────────────────────────────

.PHONY: clean-models
clean-models: ## Remove all generated models
	$(call log_progress,Cleaning generated models...)
	@rm -f $(PYTHON_ERE_MODEL) $(PYTHON_CORE_MODEL) $(JSON_SCHEMA_PATH)
	$(call log_done,Generated models cleaned.)

.PHONY: clean-doc
clean-doc: ## Remove generated docs and diagrams
	$(call log_progress,Cleaning generated documentation...)
	@rm -rf $(MODEL_DOCS_DIR)/*.md $(MODEL_DOCS_DIR)/*.svg
	$(call log_done,Generated documentation cleaned.)

.PHONY: clean
clean: clean-models clean-doc ## Remove all generated files
	$(call log_done,All generated files cleaned.)
