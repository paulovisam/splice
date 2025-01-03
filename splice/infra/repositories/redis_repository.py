import redis
from splice.infra.database import redis_session

class RedisRepository:
    def __init__(self):
        self.redis = redis_session

    def add_client_ws(self, chat_id, websocket):
        self.redis.sadd(chat_id, websocket)

    def remove_client_ws(self, chat_id, websocket):
        self.redis.srem(chat_id, websocket)

    def get_clients_ws(self, chat_id):
        return self.redis.smembers(chat_id)