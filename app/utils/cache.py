import redis
import os

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

def get_cached_response(question):
    return redis_client.get(question)


def set_cached_response(question, response):
    redis_client.set(question, response)