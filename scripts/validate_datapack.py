#!/usr/bin/env python3

"""Script to validate example datapack against the ghga-metadata-schemapack definition"""

from pathlib import Path

from schemapack import load_datapack, load_schemapack
from schemapack._internals.validation import SchemaPackValidator

ROOT = Path(__file__).parent.parent.resolve()
SCHEMAPACK_PATH = ROOT / "build" / "ghga_metadata_schema.resolved.schemapack.yaml"
DATAPACK_PATH = ROOT / "example_data" / "complete.datapack.yaml"


my_datapack = load_datapack(DATAPACK_PATH)
my_schemapack = load_schemapack(SCHEMAPACK_PATH)
schemapack_validator = SchemaPackValidator(schemapack=my_schemapack)

schemapack_validator.validate(datapack=my_datapack)