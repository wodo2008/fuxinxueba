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


class AnsModel(object):
    def __init__(self):
        conf = DATABASES
        quesnaire_mongo = pymongo.MongoClient(conf['quesnaire_mongo']['host'])
        self.answ_table = quesnaire_mongo.questionnaire.answers


    #保存问题的相关信息
    def save_ans(self,ans):
        ans_id = self.get_ans_index()
        ans['_id'] = ans_id
        self.answ_table.save(ans)

    def get_ans_index(self):
        ans_index_key = 'ans_unique_key'
        return self.quesnaire_rdb.incr(ans_index_key)