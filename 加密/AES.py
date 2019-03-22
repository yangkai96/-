from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import random,string,datetime,base64

starttime = datetime.datetime.now()
class PrpCrypt(object):

    def __init__(self, key):
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC
    def encrypt(self, text):
        text = text
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        # 这里密钥key 长度32 （AES-256）Bytes 长度
        length = 32
        count = len(text)
        if count < length:
            add = (length - count)
            text = text + ('\0' * add).encode('utf-8')
        elif count > length:
            add = (length - (count % length))
            text = text + ('\0' * add).encode('utf-8')
        self.ciphertext = cryptor.encrypt(text)
        return b2a_hex(self.ciphertext)
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        plain_text = cryptor.decrypt(a2b_hex(text))
        return bytes.decode(plain_text).rstrip('\0')
def hzname(file):
    global passname, jiamihou,jmhz,newname
    newname = file.split(".")
    passname = newname[0] + ".key"
    jmhz=str(newname[0]+'.'+newname[1])

if __name__ == '__main__':
    # 初始化密钥
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 32))
    pc = PrpCrypt(salt)
    file = input("输入要加密的文件名：").lower()
    hzm = file + '.Aes'
    hzname(hzm)
    with open(passname, "w") as f:  #秘钥保存
        f.write(salt)
    f.close()
    with open (file,"rb") as f:#读取文件
        data=base64.b64encode(f.read())
    f.close()
    e = pc.encrypt(data)  # 加密
    with open(hzm,"wb") as f:
        f.write(e)
    f.close()
    d = pc.decrypt(e)  # 解密
    with open(jmhz,"wb") as f:
        f.write(base64.b64decode(d))
    f.close()
    print("秘钥：",salt)
    print("加密后:", e)
    endtime = datetime.datetime.now()
    print("用时" + str(endtime - starttime))
