import os
from lib.conf.config import setting
class Disk(object):
    def __init__(self):
        pass

    @classmethod
    def initial(cls):
        return cls()

    def process(self,command_func,debug):
        if debug:
            output = open(os.path.join(setting.BASE_DIR, 'file/memory.out'), 'r', encoding='utf-8').read()
        else:
            output = command_func('sudo dmidecode -q -t 17 2>/dev/null')
        return self.parse(output)

    def parse(self,content):
        response = {
            '5':{
                'pd_type':'SATA',
                'slot':'5',
                'capacity':'281.231',
                'model':'SESDSDFSADAS DASF Sumsung sf'
            },
            '2': {
                'pd_type': 'SAS',
                'slot': '1',
                'capacity': '281.231',
                'model': 'SESDSDFSADAS DASF'
            }
        }

        return response