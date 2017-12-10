#!-*-coding:utf-8
import pymongo
import redis
'''
调查问卷的问题模型
'''

def init_redis(host,port,db,password=None):
    if password:
        pool = redis.ConnectionPool(host=host, port=int(port),db=int(db),password=password)
    else:
        pool = redis.ConnectionPool(host=host, port=int(port),db=int(db))
    return redis.Redis(connection_pool=pool)

class QuesModel(object):
    def __init__(self,conf):
        quesnaire_mongo = pymongo.MongoClient(conf['quesnaire_mongo']['host'])
        self.quest_table = quesnaire_mongo.questionnaire.questions


    #根据id获取问题详情
    def get_ques_by_id(self,ques_id):
        query = {'_id':ques_id}
        return self.quest_table.find_one(query)

