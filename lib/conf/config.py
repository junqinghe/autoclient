
from . import groble_settings
from conf import settings

# for name in dir(groble_settings):
#     if name.isupper():
#         value = getattr(groble_settings, name)
#         print(value)
class Settings(object):
    #########整合的配置文件#####
    def __init__(self):
        # settings_module=os.environ['USER_SETTINGS']
        #找到默认配置
        for name in dir(groble_settings):
            if name.isupper():
                value = getattr(groble_settings, name)
                setattr(self, name, value)
        #找到自定义配置
        # settings_module=os.environ.get('USER_SETTINGS')
        # if not settings_module:
        #     return
        # m=importlib.import_module(settings_module)
        for name in dir(settings):
            if name.isupper():
                value=getattr(settings,name)
                print(value)
                setattr(self,name,value)

setting=Settings()