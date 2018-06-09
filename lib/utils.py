from lib.conf.config import settings
from Crypto.Cipher import AES
def encrypt(message):
    '''
    数据加密
    :param message:
    :return:
    '''
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


def auth():

    import hashlib
    '''获取未采集的主机列表'''
    import time
    ctime = time.time()
    new_key = "%s|%s" % (settings.OPENKEY, ctime)  # 结合
    m = hashlib.md5()
    m.update(bytes(new_key, encoding='utf-8'))
    md5_key = m.hexdigest()

    md5_time_key = "%s|%s" % (md5_key, ctime)
    return md5_time_key