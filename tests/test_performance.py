import pytest
import time
from utils.helpers import make_request
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.parametrize("endpoint_name", ["pokemon_endpoint", "invalid_pokemon_endpoint"])
@pytest.mark.parametrize("test_value_index", [0, 1, 2])
def test_performance(endpoint_name, test_value_index, config, base_url):
    endpoints = config['endpoints']
    selected = [e for e in endpoints if e['name'] == endpoint_name][0]

    if test_value_index >= len(selected['test_values']):
        pytest.skip("No more test values for this endpoint")

    test_value = selected['test_values'][test_value_index]
    path = selected['path'].replace("{name}", test_value)
    url = f"{base_url}{path}"

    max_time = selected.get('max_response_time_ms', config['performance_threshold']['default_max_response_time_ms'])

    start_time = time.time()
    response = make_request("GET", url)
    elapsed = (time.time() - start_time) * 1000  # convert to ms

    logger.info(f"Performance test for {url}: {elapsed:.2f} ms")
    assert elapsed <= max_time, f"Response took {elapsed}ms, exceeding {max_time}ms"