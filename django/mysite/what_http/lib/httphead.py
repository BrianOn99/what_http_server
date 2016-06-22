import requests
import redis

cache = redis.StrictRedis(host='redis', port=6379, db=0)
not_foound_value = b"NOT_FOUND"

def find_server(url):
    cached_result = cache.get(url);
    if cached_result != None:
        print("Using cached result")
        return None if (cached_result == not_foound_value) else cached_result

    try:
        response = requests.head(url)
        result = response.headers['server']
        cache.set(url, result)
        return result;
    except requests.exceptions.MissingSchema:
        raise ValueError
    except KeyError:
        cache.set(url, not_foound_value)
        return None
