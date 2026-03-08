import redis

redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

def get_cached_response(question):
    return redis_client.get(question)


def set_cached_response(question, response):
    redis_client.set(question, response)