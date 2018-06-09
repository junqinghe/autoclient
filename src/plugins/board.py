from lib.conf.config import setting
class Board(object):
    def __init__(self):
        pass

    @classmethod
    def initial(cls):
        return cls()

    def process(self,command_func,debug):
        response={
            'manufacturer':'Paralles software internetional Inc.',
            'model':'Paralles Platform',
            'sn':'Paralles-122444'
        }           #目前数据都是假的，不完整，主要是测试用而已
        return response