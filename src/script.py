from lib.conf.config import setting
from .client import Agent,SSHSALT

def run():
    if setting.MODE=='AGENT':
        obj=Agent()   #不需要向api请求主机
    else:
        obj=SSHSALT()   #需要向api请求未检查主机
    obj.execute()
