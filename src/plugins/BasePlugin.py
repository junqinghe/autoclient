#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import commands
import paramiko
from lib.conf.config import setting



class BasePlugin(object):

    def __init__(self,hostname,username,port):
        self.hostname = hostname
        self.username = username
        self.port = port

    def os_platform(self):
        output = self.exec_shell_cmd('uname')
        return output.strip()

    def os_version(self):

        try:
            output = self.exec_shell_cmd('cat /etc/issue')
            result = output.strip().split('\n')[0]
        except Exception as e:
            result = " "
        return result

    def os_hostname(self):
        output = self.exec_shell_cmd('hostname')
        return output.strip()

    def exec_shell_cmd(self,cmd):
        private_key_path = setting.configration['key_path']
        key = paramiko.RSAKey.from_private_key_file(private_key_path)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.hostname, port=self.port, username=self.username, pkey=key)
        stdin,stdout,stderr = ssh.exec_command(cmd)
        result = stdout.read()
        ssh.close()
        return result

    def execute(self):
        return self.linux()

    def linux(self):
        raise Exception('You must implement Linux method.')
