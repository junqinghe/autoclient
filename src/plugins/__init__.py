from lib.conf.config import setting
import importlib
import traceback
class PluginsManager(object):
    def __init__(self,hostname=None):
        self.hostname=hostname
        self.plugin_dict=setting.PLUGINS_DICT
        self.mode=setting.MODE
        self.debug=setting.DEBUG
        if self.mode=='SSH':
            self.ssh_pwd=setting.SSH_PWD
            self.ssh_port=setting.SSH_PORT
            self.ssh_user = setting.SSH_USER
            self.ssh_key=setting.SSH_PRIMARY_KEY

    def exec_plugins(self):
        '''
        获取所有的插件，并执行获取插件的返回值
        :return:
        '''
        response = {}
        for k,v in self.plugin_dict.items():

            ret={'status':True,'data':None}
            try:
                module_path,class_name= v.rsplit('.',1)
                m=importlib.import_module(module_path)
                cls=getattr(m,class_name)     #找到插件
                if hasattr(cls,'initial'):    ###可在插件处理之前做点其他操作
                    obj=cls.initial()
                else:
                    obj=cls()
                result=obj.process(self.command,self.debug)   ###把交给各个插件去处理
                ret['data']=result
            except Exception as e:
                ret['status']=False
                ret['data']='[%s][%s]采集数据出现错误：%s'%(self.hostname if self.hostname else 'AGENT',k,traceback.format_exc())

            response[k]=ret
            # print(k,response)

        return response

    def command(self,cmd):
        '''返回各个模式后的结果'''
        if self.mode=='AGENT':
            return self.__agent(cmd)
        elif self.mode=='SSH':
            return self.__ssh(cmd)
        elif self.mode=='SALT':
            return self.__salt(cmd)



    def __agent(self,cmd):
        import subprocess
        output =subprocess.getoutput(cmd)
        return output
    def __ssh(self,cmd):
        #私钥方式
        import paramiko
        private_key=paramiko.RSAKey.from_private_key_file(self.ssh_key)
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.hostname,port=self.ssh_port,username=self.ssh_user,pkey=self.ssh_key,)
        stdin,stdout,stderr=ssh.exec_command(cmd)

    def __salt(self,cmd):
        #####py2###
        # import salt.client
        # local=salt.client.localClient()
        # result=local.cmd(self.hostname,'cmd.run',[cmd])
        # return result[self.hostname]

        #####py3###
        import subprocess
        result=subprocess.getoutput('salt "%s" cmd.run "%s"'%(self.hostname,cmd))
        return result