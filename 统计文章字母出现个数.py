import re,time
import matplotlib.pyplot as plt
filname=input("请输入文件名：")
with open(filname,'r',encoding='gbk') as f:
    datas=f.read()
number={}
shuju,biaoqian=[],[]
data=re.sub('[^a-zA-Z]',"",datas).lower() #[^abc] 匹配除了a,b,c之外的字符。
print('总长度:'+str(len(data)))
for n in range(97,123):
    number[chr(n)]=0
for i in data:
    for key,value in number.items():
        if (i==key):
            number[key]+=1
f.close()
for key,value in number.items():
    print(key+":",value,end="")
    shuju.append(value)
    biaoqian.append(key)
    print("\t"+"占比为：{:.2%}".format(value/len(data)))
#画图
plt.bar(range(1,27),shuju,color='rgb',tick_label=biaoqian)
plt.show()
time.sleep(30)