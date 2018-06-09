from src.plugins import PluginsManager
from lib.conf.config import setting
import requests
import json
from lib.utils import encrypt,auth
class Base(object):
    def post_asset(self,server_info):
        '''向api发送资产信息'''
        data=encrypt(json.dumps(server_info))
        requests.post(setting.API,data=data,headers={'ContentType':'application/json','Openkey':auth()})    #json打包发过去，会默认发送一个header={'content-type':'application/json'},所有接受方只能在request.body里面接受到，request.post是没有值的
        ##json.loads(request.body())

class Agent(Base):   #继承上面
    '''agent模式'''
    def execute(self):
        server_info =PluginsManager().exec_plugins()
        hostname=server_info['basic']['data']['hostname']

        certname=open(setting.CERTNAME_PATH,'r',encoding='utf-8').read().strip()
        if not certname:      #第一次写入主机号
            with open(setting.CERTNAME_PATH,'w',encoding='utf-8')as f:
                f.write(hostname)
        else:
            server_info['basic']['data']['hostname']=certname
        self.post_asset(server_info)


class SSHSALT(Base):
    '''paramiko 和 saltstack'''
    def get_post(self):
        import json
        import hashlib
        '''获取未采集的主机列表'''
        import time
        ctime = time.time()
        new_key = "%s|%s" % (setting.OPENKEY, ctime)  # 结合
        m = hashlib.md5()
        m.update(bytes(new_key, encoding='utf-8'))
        md5_key = m.hexdigest()

        md5_time_key="%s|%s"%(md5_key,ctime)

        response=requests.get(setting.API,headers={'Openkey':auth()})       #获取请求的时候要做api验证
        result=json.loads(response.text)
        if not result['status']:
            return
        else:
            return result['data']   #{'status':true,'data':['c1.com,'c2.com']}  主机列表

    def run(self,host):
        server_info = PluginsManager(host).exec_plugins()
        self.post_asset(server_info)
    def excute(self):
        from concurrent.futures import ThreadPoolExecutor
        host_list=self.get_post()
        pool=ThreadPoolExecutor(max_workers=10)
        for host in host_list:
            # server_info=PluginsManager(host).exec_plugins()
            # self.post_asset(server_info)
            pool.submit(self.run,host)
