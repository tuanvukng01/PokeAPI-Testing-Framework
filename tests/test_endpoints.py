import pytest
from utils.helpers import make_request
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.parametrize("endpoint_config", [
], indirect=True)
def test_endpoint_reachability(endpoint_config, base_url):
    url, expected_status, _ = endpoint_config
    logger.info(f"Testing endpoint reachability for URL: {url}")
    response = make_request("GET", url)
    assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}"

@pytest.fixture(params=["pokemon_endpoint", "invalid_pokemon_endpoint"])
def endpoint_config(request, config, base_url):
    endpoints = config['endpoints']
    selected = [e for e in endpoints if e['name'] == request.param][0]
    expected_status = selected['expected_status']


    return (None, None, None)

@pytest.mark.parametrize("endpoint_name", ["pokemon_endpoint", "invalid_pokemon_endpoint"])
@pytest.mark.parametrize("test_value_index", [0, 1, 2])  # Attempt to cover multiple test values
def test_endpoint_status(endpoint_name, test_value_index, config, base_url):
    endpoints = config['endpoints']
    selected = [e for e in endpoints if e['name'] == endpoint_name][0]

    if test_value_index >= len(selected['test_values']):
        pytest.skip("No more test values for this endpoint")

    test_value = selected['test_values'][test_value_index]
    expected_status = selected['expected_status']

    path = selected['path'].replace("{name}", test_value)
    url = f"{base_url}{path}"

    logger.info(f"Testing status code for URL: {url}")
    response = make_request("GET", url)
    assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}"