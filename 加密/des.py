from pyDes import des, CBC, PAD_PKCS5
import binascii,random,string
key = ''.join(random.sample(string.ascii_letters + string.digits, 8))        # 生成随机8位秘钥
iv = b"\0\0\0\0\0\0\0\0"   #偏转向量
def des_encrypt(s):
    k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    print("加密：\t"+str(en))
    return binascii.b2a_hex(en)
def des_descrypt(s):
    k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    print("解密：\t"+str(de,encoding="utf-8"))
data=input("请输入数据：").encode()
print("秘钥：\t"+key)
jiami=des_encrypt(data)
jiemi=des_descrypt(jiami)