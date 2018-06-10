from lib.conf.config import setting
import os
class Basic(object):
    def __init__(self):
        pass

    @classmethod
    def initial(cls):
        return cls()

    def process(self,command_func,debug):
        # if debug:
        #     output=open(os.path.join(setting.BASE_DIR,'file/cpuinfo.out'),'r',encoding='utf-8').read()
        # else:
        #     output = command_func('cat /proc/cpuinfo')
        # return self.prase(output)

        output={
            'os_platform':'linux',
            'os_version':'CentOS release 6.6 (final)\nKernel \r on an \m',
            'hostname':'junqing.com'
        }
        return self.prase(output)
    def prase(self,content):
        return content
