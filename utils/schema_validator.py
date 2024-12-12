import json
import jsonschema
from jsonschema import validate
from utils.logger import get_logger

logger = get_logger(__name__)

def validate_json_schema(data, schema_path):
    with open(schema_path, 'r') as schema_file:
        schema = json.load(schema_file)
    try:
        validate(instance=data, schema=schema)
        return True, None
    except jsonschema.exceptions.ValidationError as e:
        logger.error(f"Schema validation error: {e.message}")
        return False, e.message