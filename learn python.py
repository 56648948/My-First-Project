# 注释，可选中然后ctrl+/键
# 1.变量
print("hello world")
a = 1
b = 3
print(a + b)
print(a * b)  # 还有左除、右除
# 2.字符串
string1 = "我是\n第一个字符串"  # 转义字符：\n换行   \"   \\
string2 = "我是\"第一个字符串"
string3 = "我是\\第一个字符串"
print(string1)
print(string2)
print(string3)

string4 = "我是第一个字符串"
string5 = "我是第二个字符串"
print(string4 + string5)
print(string4[0])  # 取字符串中的某些片段,0代表“我”，-1代表倒数第一个“串”
print(string4[0:4])  # 不包括4,左闭右开


# 3.函数
def get_sum(sum1, sum2):  # define  sum1=a sum2=b
    result = sum1 + sum2
    return result


a = 1
b = 3
c = get_sum(a, b)
print(c)


# 4.类
class Person:
    def __init__(self, name, height, weight):  # self目前使用的实例
        self.name = name
        self.height = height
        self.weight = weight

    def say_name(self):
        print("我的名字叫" + self.name)

    def say_hello(self, target_name):
        print("我叫" + self.name + "，很高兴见到你" + target_name)


person1 = Person("老张", 170, 100)  # 实例
person2 = Person("老王", 160, 80)

person1.say_name()
person2.say_name()
print(person1.height)

person1.say_hello("老邓")

# 5.整数，浮点数，数字函数
# int（eger）,float(小数)，complex(复数)
a = 1  # 整数
a = 1.0  # 浮点数
b = 3
print(a + b)  # 加减运算中若有浮点数，则结果是浮点数
print(a / b)  # 除法运算不论类型结果都是浮点数
print(a // b)  # 整除出来的结果是整数，去掉小数点
print(float(a))  # 整数形式a转换为浮点数
print(int(a))  # 浮点数形式a转换成整数，直接去掉小数点

a = -2
# abs (absolute)绝对值
print(abs(a))
# round  五舍六入
print(round(a))
# pow(power)  取幂
print(pow(a, 2))  # 参数：底，指数
# ceil  大于目前值的最小的整数；     在使用之前要先调用模块math;      模块：别人写好的脚本文件，包括函数、类等等，类似C语言的头文件
import math

print(math.ceil(a))
print(math.floor(a))  # 与ceil相反的是floor

# 6.字符串方法，官方文档使用，函数默认值
string6 = "我是第一个字符串"
# len(length)
print(len(string6))
# capitalize  把字符串的第一个首字母大写
string7 = "hello word"
print(string7.capitalize())
# upper  把字符串的所有字母大写
print(string7.upper())
# lower  把字符串的所有字母小写
string8 = "HLLO"
print(string8.lower())
# replace 替换文字
print(string8.replace("HLLO", "HELLO"))
# find  返回字符串在s[start:end]切片内被找到的最小索引；未被找到返回值为-1
print(string7.find("llo"))  # 返回值为2
# boolean 布尔  只有下面两个值
a = True  # 一定要大写
b = False
# isupper   判断是否都是大写   is判断
print(string7.isupper())


# split  返回一个由字符串内单词组成的列表，使用sep作为分隔字符串   （sep=None,maxsplit=-1）
# 若未指定为-1，则不限制拆分次数
# 引例
def get_sum(sum1, sum2=4):  # 有默认值的参数要放在后边
    return sum1 + sum2


print(get_sum(1))  # 结果为5，因为sum2默认值为4
# split
string9 = "hello world!"
print(string9.split('o'))  # 不加后一个参数就不会限制切割次数
print(string9.split('o', 1))
# endswith  如果字符串以指定的后缀结束返回True，否则返回False
print(string9.endswith("world!"))

# 7.列表与元组  列表[]可以理解成一个容器，可取可放有顺序，放的是不同数据类型的数据 如list1=["wo",True,[9.5],2,3,4,5]
# 在使用时，基本上一个列表里面的每一项是同一类型
list1 = [1, 2, 3, 4, 5]
print(list1[0])  # 访问
list.append(6)  # append添加列表中的项
list.pop()  # pop删除列表中的项 默认是删掉列表中的最后一项
print(len(list1))  # 获得列表长度
list1.insert(0, 1)  # (相应位置，添加元素)
print(list1)

list2=[1,3,2,4,5]
list.sort()#排列
print(list1.index(2))    #返回“2”元素的索引（位置）
list1.reverse()   #列表取反
print(list1)
list1

list1.remove(3)   #删掉“3”
list1[1]=9   #第1个索引改为“9”

#元组：不能修改的列表()  tuple
tuple1=(1,2,3)
print(len(tuple1))
print(tuple1[0])
#列表与元组的转换
print(list(tuple1))
tuple(list1)

#8.字典{} dict(dictionary) 也可称是一个容器，里面存放的是键值
dict1={"name":"老张","height":170,"weight":100}    #“name”键：必须是字符串的格式，后面必须跟：后面的值可以是任何类型
print(dict1["name"])   #访问
print(len(dict1))    #获得键值对的数目  3
print(dict1.keys())    #获得所有的键并放到列表里
print(dict1.values())   #获得所有的值

dict1["name"]="老邓"    #修改键值对
dict1["gender"]="男"   #添加键值对
print(dict1)

dict1.pop("name")  #删除name键值对

#9.集合 set {}或（（））  也是一个容器，跟列表的区别在于里面的元素不能重复，元素没有顺序
set1={1,2,3,5,2}
print(set1)  #最后结果中把重复的2删掉了
#另一种写法
set=set((2,3,1,5,7))   #结果自动从1开始排序
print(set1[0])   #会报错，集合没有索引的概念

set2={1,2,3,4}
set2.add(5)       #添加元素5
set2.discard(3)   #删除元素3

set3={3,4,5}
set4={1,2,3,4,5,6}
print(set3.intersection(set4))   #集合取交集
print(set3.difference(set4))   #前减后，输出两个集合的差集
print(set4.difference(set3))
print(set4.issubset(set3))    #set4是否是set3的子集

#10.值类型变量与引用类型变量
#值类型：数字  布尔
a=1
b=a   #仅仅是值传递，没有地址问题
b=3
print("a:"+str(a))   #a加冒号打输出就是加冒号的，str则是将变量变为字符串
print("b:"+str(b))   #输出结果虽然看起来一样，但实际上把数字1变为了字符1

#引用类型：列表 元组 字典 集合 字符串
list3=[1,2,3]
list4=list3   #地址传递
#list4=[2,3,4]  # 重新申请一个地址
list4[1]=4    #共用一个地址，直接改地址里面的
print("list3"+str(list3))
print("list4"+str(list4))

#11.条件控制：在不同的条件下去执行不同的代码块
homework_finished=True
if (homework_finished):
    print("你可以去看会电视")
else:
    print("滚去写作业")

# > < >= <= == !=
price=1000
expensive=(price>800)
print(expensive)

if (price>800):
    print("你这也太贵了")
elif (price>600):   #else if
    print("还是有点贵")
elif (price>400):
    print("能不能再少点")
elif (price>200):
    print("可以接受")
else:
    print("买了")


#12.循环
a=10
while(a>5):
    print(a)
    a=a-1
    if(a==8):
        break
print("循环结束")

#序列：字符串  列表  元组
string10="shuihoaap"
for char in string10:  #char:自己命名的变量名  会依次把string10的每个字母赋给char
    print(char)

#法一
list5=["老邓","老张","老王"]
for person in list5:
    print(person)
#法二
#引例 print(list(range(0,10,2)))  #创建列表  [0,12),步长为2
for i in range(0,len(list5),1):   #此处0和1可以省略掉
    print(list5[i])
#创造0-9的序列
for i in range(10):
    print(i)
    if(i==5):
        break
#break跳出循环关键字

patients=[False,True,False,True]
for patient in patients:
    if(patient):
        continue   #跳过下面print的内容，直接执行下一个循环
    print("治疗这个病人")

#13.模块：详看module tutorial文件