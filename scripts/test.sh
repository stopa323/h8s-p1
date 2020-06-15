#!/usr/bin/env bash

set -e
set -x

bash ./scripts/lint.sh
pytest --disable-warnings --cov=base --cov=tests --cov-report=term-missing tests/