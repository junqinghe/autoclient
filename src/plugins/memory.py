from lib.conf.config import setting
class Memory(object):
    def __init__(self):
        pass
    @classmethod
    def initial(cls):
        return cls()
    def process(self,command_func,debug):
        "grep 'MemTotal\|MemFree\|Buffers\|^Cached\|SwapTotal\|SwapFree' /proc/meminfo"
        response = {
            # 'DIMM #2': {
            #     'manufacture':'not Special',
            #     'capacity':'500m',
            #     'slot':'DIMM #2',
            #     'speed':'667MHz',
            #     'model':'DRAM',
            #
            # }
            '2': {
                'manufacture': 'not Special',
                'capacity': '500m',
                'slot': 'DIMM #2',
                'speed': '667MHz',
                'model': 'DRAM',
            }
        }
        return response