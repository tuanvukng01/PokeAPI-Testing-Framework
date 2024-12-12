#!/bin/bash

mkdir -p config
mkdir -p tests
mkdir -p utils
mkdir -p reports
mkdir -p .github/workflows

touch config/config.yaml
touch config/schema_pokemon.json
touch tests/conftest.py
touch tests/test_data_validation.py
touch tests/test_endpoints.py
touch tests/test_performance.py
touch utils/helpers.py
touch utils/logger.py
touch utils/schema_validator.py
touch .github/workflows/ci.yaml
touch requirements.txt
touch README.md

echo "Folder structure created successfully!"