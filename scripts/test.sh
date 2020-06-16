#!/usr/bin/env bash

set -e
set -x

bash ./scripts/lint.sh
pytest --disable-warnings \
       --verbose \
       --cov=p1 \
       --cov-branch \
       --cov-report=term-missing \
       --cov-fail-under=80 \
       --no-cov-on-fail \
       tests/