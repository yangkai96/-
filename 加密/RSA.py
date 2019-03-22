import rsa,datetime
starttime=datetime.datetime.now()
key = rsa.newkeys(4096)#生成随机秘钥
privateKey = key[1]#私钥
publicKey = key[0]#公钥
#保存密钥
with open('private1.pem','w+') as f:
    f.write(privateKey.save_pkcs1().decode())
with open('public1.pem','w+') as f:
    f.write(publicKey.save_pkcs1().decode())
# 导入密钥
with open('public1.pem', 'r') as f:
    publicKey = rsa.PublicKey.load_pkcs1(f.read().encode())
with open('private1.pem', 'r') as f:
    privateKey = rsa.PrivateKey.load_pkcs1(f.read().encode())

#加密
data=''
with open('password.txt','rb') as f:
    data=f.read()
cryptedMessage = rsa.encrypt(data, publicKey)
f.close()

#加密后输出
with open('加密后.txt','wb')as f:
    f.write(cryptedMessage)
f.close()

#解密
with open('解密后.txt','wb')as f:
    datas=rsa.decrypt(cryptedMessage, privateKey)
    f.write(datas )
f.close()
endtime=datetime.datetime.now()
print("用时"+str(endtime-starttime))