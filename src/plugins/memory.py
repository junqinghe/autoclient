from lib.conf.config import setting
import os
from lib import convert
class Memory(object):
    def __init__(self):
        pass
    @classmethod
    def initial(cls):
        return cls()

    def process(self, command_func, debug):
        if debug:
            output = open(os.path.join(setting.BASE_DIR, 'file/disk.out'), 'r', encoding='utf-8').read()
        else:
            output = command_func('sudo dmidecode  -q -t 17 2>/dev/null')

        return self.parse(output)

    def parse(self,content):

        ram_dict = {}
        key_map = {
            'Size':'capacity',
            'Locator':'slot',
            'Type':'model',
            'Speed':'speed',
            'Manufacturer':'manufactory',
            'Serial Number':'sn',

        }
        devices = content.split('Memory Device')
        for item in devices:
            item = item.strip()
            if not item:
                continue
            if item.startswith('#'):
                continue
            segment = {}
            lines = item.split('\n\t')
            for line in lines:
                if len(line.split(':'))>1:
                    key,value = line.split(':')
                else:
                    key = line.split(':')[0]
                    value = ""
                if key_map.has_key(key):
                    if key == 'Size':
                        segment[key_map['Size']] = convert.convert_mb_to_gb(value,0)
                    else:
                        segment[key_map[key.strip()]] = value.strip()
            ram_dict[segment['slot']] = segment

        return ram_dict