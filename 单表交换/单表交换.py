mingwen=list(input("请输入要交换的明文：\n").lower())
k=int(input("请输入移位值k:\n"))
miwen=[]
print("密文:\t",end="")
for i in mingwen:  #循环交换加密
    p=chr(ord(i)+k)
    miwen.append(p)
    print(p,end="")
print("\n解密后:\t",end="")#解密后输出
for n in miwen:
    m=chr(ord(n)-k)
    print(m,end="")