import yaml
import requests
import time
from functools import wraps
from utils.logger import get_logger

logger = get_logger(__name__)

def load_config(path="config/config.yaml"):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def make_request(method, url, retries=3, delay=1, **kwargs):
    for attempt in range(1, retries+1):
        try:
            response = requests.request(method, url, **kwargs)
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error: {e}, attempt {attempt}/{retries}")
            if attempt < retries:
                time.sleep(delay)
            else:
                raise