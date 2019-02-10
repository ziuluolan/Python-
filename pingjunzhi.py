#1,编写 储存数据 函数
def getnumber():
    numbers=[]
    n=input("请输入要计算的数字: ")
    while int(n)<7:
        numbers.append(int(n))
        n=input("请输入要计算的数字: ")
    return numbers
#2,编写 各计算函数
#计算平均值
def junzhi(numbers):
    s=0.0
    for i in numbers:
        s+=i
        j=s/len(numbers)
    return j
#计算方差
def fangcha(numbers,junzhi):
    sdev=0.0
    for i in numbers:
        sdev+=pow((i-junzhi),2)
        f=pow(sdev/(len(numbers)-1),2)
        return f
#计算中位数
def zhongweishu(numbers):
    #偶数的中位数计算
    #numbers.sort()
    s=len(numbers)
    if s%2==0:
        z=(numbers[s//2-1]+numbers[s//2+1])/2
    else:
        z=numbers[s//2]
    return z
 
#3,编写输出函数
n=getnumber()
print('平均值{} 中位数{} 方差{}'.format(junzhi(n),zhongweishu(n),fangcha(n,junzhi(n))))







