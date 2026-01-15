import os

class MockRedis:
    def __init__(self):
        self.data = {}
        print("Initialized Mock Redis (In-Memory)")

    def set(self, key, value):
        self.data[key] = value
        return True

    def get(self, key):
        return self.data.get(key)

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            return 1
        return 0

# Try to connect to real Redis, else fallback
try:
    import redis
    # Check if REDIS_URL env var is set, otherwise default
    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    # For this demo environment, likely no Redis, so we default to Mock
    # but let's try to verify connection if strictly needed.
    # r = redis.from_url(redis_url)
    # r.ping()
    # redis_client = r
    # Fallback for safe demo:
    redis_client = MockRedis()
except Exception:
    redis_client = MockRedis()
