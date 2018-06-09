import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

#####用户变量
os.environ['USER_SETTINGS']='conf.settings'

#######整体变量
from lib.conf.config import setting
# print('################',setting.__dict__)
from src.plugins import PluginsManager
from src import script
if __name__ == '__main__':
    script.run()



###需要：
# 主机名不重复
# 流程标准化：装机时，主机名在cmdb的client设置好了