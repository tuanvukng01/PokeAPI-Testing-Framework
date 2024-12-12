import pytest
from utils.helpers import make_request
from utils.schema_validator import validate_json_schema
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.parametrize("test_value", ["pikachu", "bulbasaur", "charizard"])
def test_data_schema(test_value, config, base_url):
    pokemon_schema_path = config['schema_validation']['pokemon_schema']
    path = "/pokemon/" + test_value
    url = f"{base_url}{path}"

    logger.info(f"Validating schema for URL: {url}")
    response = make_request("GET", url)
    assert response.status_code == 200, f"Expected status 200 for {url}, got {response.status_code}"

    data = response.json()
    valid, error = validate_json_schema(data, pokemon_schema_path)
    assert valid, f"Schema validation failed for {url}: {error}"