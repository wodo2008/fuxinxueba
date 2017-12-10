from questionnaire.ansModel import AnsModel
from questionnaire.userModel import UserModel
import time

class QuestService(object):
    def __init__(self):
        self.ans_obj = AnsModel()
        self.user_obj = UserModel()


    def save_ans(self,param):
        ans_info = {}
        ans_info['ques_id'] = param.get('ques_id','')
        ans_info['user_id'] = param.get('user_id','')
        ans_info['ans'] = param.get('ans','')
        ans_info['time'] = int(time.time())
        self.ans_obj.save_ans(ans_info)
        return True

    def save_user_info(self,param):
        user_info = {}
        user_info['full_name'] = param.get('full_name','')
        user_info['chinese_name'] = param.get('chinese_name','')
        user_info['snumber'] = param.get('snumber','')
        return self.user_obj.save_user_info(user_info)


