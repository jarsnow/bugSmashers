import redis
from creds import redis_host, redis_port, redis_password

def setup_redis(redis_host, redis_port, redis_password):
    r = redis.Redis(
    host=redis_host,
    port=redis_port,
    password=redis_password)

    return r

r = setup_redis("redis-11661.c1.asia-northeast1-1.gce.cloud.redislabs.com",11661, redis_password)

r.set('foo', 'bar')
# True

print(r.get('foo'))

