import rsa, base64

######生成公钥私钥######
# pub_key_obj, priv_key_obj = rsa.newkeys(256)  # 指定长度，32个字节
# pub_key_str = pub_key_obj.save_pkcs1()
# pub_key_code = base64.standard_b64encode(pub_key_str)
# priv_key_str = priv_key_obj.save_pkcs1()
# priv_key_code = base64.standard_b64encode(priv_key_str)
#
#
# #####加密######
# def encrypt(value):
#     key_str = base64.standard_b64encode(pub_key_code)
#     pk = rsa.Publickey.load_pkcs1(key_str)
#     val = rsa.encrypt(value.encode('utf-8'), pk)
#     return val
#
#
# #####解密######
# def decrypt(value):
#     key_str = base64.standard_b64encode(priv_key_code)
#     pk = rsa.Publickey.load_pkcs1(key_str)
#     val = rsa.decrypt(value, pk)
#     return val

from Crypto.Cipher import AES

#########################加密
def encrypt(message):
    key=b'asdasfasdasdf242'  #这个tm也要16位
    cipher=AES.new(key,AES.MODE_CBC,key)   #创建对象
    ba_data=bytearray(message,encoding='utf-8')   #字节长度

    v1=len(ba_data)
    v2=v1%16
    print(v1,v2)
    if v2==0:
        v3=16
    else:
        v3=16-v2
    for i in range(v3):
        # ba_data.append(32)   #这里的32是ASCII码表第32位，空格的意思
        ba_data.append(v3)
        # print('asdasdsad')
    fina_data=ba_data
    # fi=bytes(fina_data,encoding='utf-8')
    msg=cipher.encrypt(fina_data)
    # print(msg)
    # msg=cipher.encrypt(fina_data.decode('utf-8'))    #要加密的字符串必须是16个字节或者16的倍数
    return msg           #得到密文（字节）

######################解密
def decrypt(msg):           #发送过来的是字节类型
    key=b'asdasfasdasdf242'
    cipher=AES.new(key,AES.MODE_CBC,key)   #创建对象
    result=cipher.decrypt(msg)
    num=result[-1]
    data=result[0:-num]
    print(str(data,encoding='utf-8'))
    return str(data,encoding='utf-8')



# v=encrypt('吃毛线么')
#
# print(v)
# decrypt(v)



# import paramiko
#
# # 创建SSH对象
# ssh = paramiko.SSHClient()
# # 允许连接不在know_hosts文件中的主机
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # 连接服务器
# ssh.connect(hostname='192.168.2.107' ,port=22, username='root', password='123456')
# #
# # 执行命令
#
# stdin, stdout, stderr = ssh.exec_command('dir')
# # 获取命令结果
# result = stdout.read()+stderr.read()
# ssh.close()
#
# print(result)
