from lib.conf.config import setting
import os
class Board(object):
    def __init__(self):
        pass

    @classmethod
    def initial(cls):
        return cls()

    def process(self,command_func,debug):
        if debug:
            output=open(os.path.join(setting.BASE_DIR,'file/board.out'),'r',encoding='utf-8').read()
        else:
            output = command_func('sudo dmidecode -t1')
        return self.prase(output)

    def prase(self,content):



        # response={
        #     'manufacturer':'Paralles software internetional Inc.',
        #     'model':'Paralles Platform',
        #     'sn':'Paralles-122444'
        # }           #目前数据都是假的，不完整，主要是测试用而已

        result = {}
        key_map = {
            'Manufacturer': 'manufactory',
            'Product Name': 'model',
            'Serial Number': 'sn',
        }

        for item in content.split('\n'):
            row_data = item.strip().split(':')
            if len(row_data) == 2:
                if key_map.has_key(row_data[0]):
                    result[key_map[row_data[0]]] = row_data[1].strip() if row_data[1] else row_data[1]

        return result
