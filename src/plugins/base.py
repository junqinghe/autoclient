import os
from lib.conf.config import setting

class BasePlugin(object):
    def __init__(self):
        pass
    @classmethod
    def initial(cls):
        return cls()
    def process(self,command_func,debug):
        # output = command_func('cat /proc/cpuinfo')      ##Linux上操作的命令
        if debug:
            output=open(os.path.join(setting.BASE_DIR,'file/cpuinfo.out'),'r',encoding='utf-8').read()
        else:
            output = command_func('cat /proc/cpuinfo')
        return self.prase(output)
    def prase(self,content):
        import re
        response={'cpu_count':0,'cpu_physical_count':0,'cpu_model':''}
        # v=content.split('\n')
        cpu_physical_set=set()
        content=content.strip()
        for item in content.split('\n\n'):
            for row_line in item.split('\n'):
                key,value=row_line.split(':')
                key=key.strip()
                if key=='processor':
                    response['cpu_count']+=1
                elif key=='physical id':
                    cpu_physical_set.add(value)
                elif key=='model name':
                    if  not response['cpu_model']:
                        response['cpu_model']=value
            response['cpu_physical_count']=len(cpu_physical_set)
        return response