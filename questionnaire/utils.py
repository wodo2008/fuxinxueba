#!-*-coding:utf-8-*-

import redis

global unique_key_redis

def init_redis(host,port,db,password=None):
    if password:
        pool = redis.ConnectionPool(host=host, port=int(port),db=int(db),password=password)
    else:
        pool = redis.ConnectionPool(host=host, port=int(port),db=int(db))
    return redis.Redis(connection_pool=pool)
