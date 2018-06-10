import os,sys
USER='192.168.2.107'
PWD=123456
MODE='AGENT'
DEBUG=True
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
SSH_USER='root'
SSH_PWD=123
SSH_PRIMARY_KEY='/XX/XX/XX'
SSH_PORT=22
PLUGINS_DICT={

    'basic':'src.plugins.basic.Basic',
    'board':'src.plugins.board.Board',
    'cpu':'src.plugins.cpu.Cpu',
    'disk':'src.plugins.disk.Disk',
    'memory':'src.plugins.memory.Memory',
}

OPENKEY="dasaggdsgadgag"
API='http://www.baidu.com/'

CERTNAME_PATH=os.path.join(BASE_DIR,'file','certname')
# print(CERNAME_PATH)