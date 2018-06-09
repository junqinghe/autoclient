from lib.conf.config import setting
class Basic(object):
    def __init__(self):
        pass

    @classmethod
    def initial(cls):
        return cls()

    def process(self,command_func,debug):
        # if debug:
        #     output=open()
        output={
            'os_platform':'linux',
            'os_version':'CentOS release 6.6 (final)\nKernel \r on an \m',
            'hostname':'junqing.com'
        }
        return self.prase(output)
    def prase(self,content):
        return content
