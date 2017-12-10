#!-*- coding: utf-8 -*-
import pymongo
import redis
from fuxinxueba.settings import DATABASES
'''
调查问卷的答案模型
'''
def init_redis(host,port,db,password=None):
    if password:
        pool = redis.ConnectionPool(host=host, port=int(port),db=int(db),password=password)
    else:
        pool = redis.ConnectionPool(host=host, port=int(port),db=int(db))
    return redis.Redis(connection_pool=pool)


class UserModel(object):
    def __init__(self):
        conf = DATABASES
        quesnaire_mongo = pymongo.MongoClient(conf['quesnaire_mongo']['host'])
        self.user_table = quesnaire_mongo.questionnaire.users
        ques_redis_conf = conf['quesnaire_redis']
        self.quesnaire_rdb = init_redis(ques_redis_conf['host'],ques_redis_conf['port'],ques_redis_conf['db'])

    #保存用户的相关信息
    def save_user_info(self,user_info):
        if not isinstance(user_info,dict):
            return False
        user_info['_id'] = self.get_user_index()
        self.user_table.save(user_info)
        return self.get_user_index()


    def get_user_info(self,user_id):
        query = {'_id':user_id}
        return self.user_table.find_one(query)

    def get_user_index(self):
        user_index_key = 'user_unique_key'
        return self.quesnaire_rdb.incr(user_index_key)
