#!/usr/bin/env python3
"""Script to build resolved resolved ghga-metadata-schema  schemapack definition"""


from pathlib import Path

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent.resolve()
RESOLVED_SCHEMA_PATH = ROOT / "build" / "ghga_metadata_schema.resolved.schemapack.yaml"

