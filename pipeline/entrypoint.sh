#!/bin/sh
set -e
uv run python ingest_data.py
uv run python load_green_and_zones.py