SHELL=/bin/bash -o pipefail

BUILD_PRINT = \e[1;34m
END_BUILD_PRINT = \e[0m

ICON_DONE = [✔]
ICON_ERROR = [x]
ICON_WARNING = [!]
ICON_PROGRESS = [-]

LINKML_MODEL_NAME=ere-service-schema
LINKML_MODEL_VERSION=0.1.0
PYTHON_MODEL_PATH=src/ere/models/core.py

SCHEMAS_DIR=resources/schemas

LINKML_MODEL_PATH=$(SCHEMAS_DIR)/$(LINKML_MODEL_NAME)-v$(LINKML_MODEL_VERSION).yaml
JSON_SCHEMA_PATH=$(SCHEMAS_DIR)/$(LINKML_MODEL_NAME)-v$(LINKML_MODEL_VERSION).json

MODEL_DOCS_DIR=docs/schema
MODEL_DOCS_README=$(MODEL_DOCS_DIR)/README.md

## Setup commands
#

# Note that Python, Poetry and Make are a pre-requisites and we don't deal with them here.
#

install:
	@ echo "Installing dependencies using Poetry..."
	@ poetry sync


## Quality commands
#

PYLINT_SOURCE_PATHS = ./src ./test

lint:
	@ echo -e "$(BUILD_PRINT)$(ICON_PROGRESS) Running Pylint checks$(END_BUILD_PRINT)"
	@ poetry run pylint --rcfile=.pylintrc $(PYLINT_SOURCE_PATHS)
	@ echo -e "$(BUILD_PRINT)$(ICON_DONE) Pylint checks completed$(END_BUILD_PRINT)"

lint-report:
	@ echo -e "$(BUILD_PRINT)$(ICON_PROGRESS) Running Pylint and generating report$(END_BUILD_PRINT)"
	@ poetry run pylint --rcfile=.pylintrc --recursive=y $(PYLINT_SOURCE_PATHS) | grep -E "^Your code" | sed 's/^Your code/Pylint: Your code/' > pylint_report.txt || true
	@ echo -e "$(BUILD_PRINT)$(ICON_DONE) Pylint report generated in pylint_report.txt$(END_BUILD_PRINT)"

lint-full-report:
	@ echo -e "$(BUILD_PRINT)$(ICON_PROGRESS) Running full Pylint and generating report$(END_BUILD_PRINT)"
	@ poetry run pylint --rcfile=.pylintrc $(PYLINT_SOURCE_PATHS) | sed 's/^Your code/Pylint: Your code/' > pylint_report.txt || true
	@ echo -e "$(BUILD_PRINT)$(ICON_DONE) Full Pylint report generated in pylint_report.txt$(END_BUILD_PRINT)"


## Test commands
#

test:
	@ echo -e "$(BUILD_PRINT)$(ICON_PROGRESS) Running tests$(END_BUILD_PRINT)"
	@ poetry run pytest test/ \
		--cov=ere \
		--cov-report=term \
		--cov-report=term-missing:skip-covered \
		--cov-report=xml:coverage.xml \
		-v \
		$(PYTEST_ARGS)
	@ echo -e "$(BUILD_PRINT)$(ICON_DONE) Tests completed$(END_BUILD_PRINT)"


## Build commands
#

all: $(PYTHON_MODEL_PATH) $(JSON_SCHEMA_PATH) $(MODEL_DOCS_README)

generate-models: $(PYTHON_MODEL_PATH) $(JSON_SCHEMA_PATH)
generate-doc: $(MODEL_DOCS_README)

.PHONY: all generate-models generate-doc clean clean-doc clean-models install lint lint-report lint-full-report test


$(PYTHON_MODEL_PATH): $(LINKML_MODEL_PATH)
	@ echo "Generating Python service model..."
	@ mkdir -p $(dir $(PYTHON_MODEL_PATH))
	@ poetry run linkml generate pydantic $(LINKML_MODEL_PATH) > $(PYTHON_MODEL_PATH)

$(JSON_SCHEMA_PATH): $(LINKML_MODEL_PATH)
	@ echo "Generating JSON Schema for the ERE service..."
	@ mkdir -p $(dir $(JSON_SCHEMA_PATH))
	@ poetry run linkml generate json-schema --indent 2 $(LINKML_MODEL_PATH) > $(JSON_SCHEMA_PATH)



$(MODEL_DOCS_README): $(LINKML_MODEL_PATH)
	@ echo "Generating documentation for the ERE service Schema..."
# Changing default index name from index.md to README.md, since the github browser automatically shows the latter name
# when entering the MODEL_DOCS_DIR
	@ poetry run linkml generate doc $(LINKML_MODEL_PATH) -d $(MODEL_DOCS_DIR) --index-name README
# TODO: Probably we want PNG instead, but it doesn't work yet (https://github.com/linkml/linkml/issues/3009)
	@ poetry run linkml generate plantuml -d $(MODEL_DOCS_DIR) --format svg $(LINKML_MODEL_PATH)
	
# (Brandizi) I've played with it, but the result isn't great (single-class diagrams in each 
# class file)
# @ poetry run linkml generate doc -d $(MODEL_DOCS_DIR) --diagram-type plantuml_class_diagram $(LINKML_MODEL_PATH)


clean-models:
	@ echo "Cleaning up generated models..."
	@ rm -rf $(PYTHON_MODEL_PATH) $(JSON_SCHEMA_PATH)

clean-doc:
	@ echo "Cleaning up generated documentation..."
	@ rm -rf $(MODEL_DOCS_DIR)/*.md

clean: clean-doc clean-models
	@ echo "All generated files cleaned."