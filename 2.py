#虽然名字为pytorch，但要写做导入torch
import torch
x=torch.arange(12)  # 张量表示一个数组，这个数组可能有多个维度，此处输出为0-11
x

x.shape    #通过张量的shape访问张量的形状、张量中元素的总数
x.numel()

x=x.reshape(3,4)    #要改变一个张量的形状而不改变元素数量和元素值
x

torch.zeros((2,3,4))   #使用全0、全1、其他常量或者从特定分布中随机采样的数字
torch.ones((2,3,4))

torch.tensor([[2,1,4,3],[1,2,3,4],[4,3,2,1]])  #.shape
# #通过提供包含数值的python列表（或嵌套列表）来为所需张量中的每个元素赋予确定值

#常见的标准算术运算符（+、-、*、/、**）都可以被升级为按元素运算
x=torch.tensor([1.0,2,4,8])
y=torch.tensor([2,2,2,2,])
x+y,x-y,x*y,x/y,x**y   #   **为求幂符
#按元素方式应用更多的计算
torch.exp(x)  #指数
#把多个张量连结在一起
X=torch.arange(12,dtype=torch.float32).reshape((3,4))
Y=torch.tensor([[2.0,1,4,3],[1,2,3,4],[4,3,2,1]])
torch.cat((X,Y),dim=0),torch.cat((X,Y),dim=1)   #dim=0从第0维开始合并，在这可以看成按行合并，dim=1可以看成按列合并
X==Y   #通过逻辑运算符构建二元张量
X.sum()   #对张量所有的元素求和会产生一个只有一个元素的张量

#即使形状不同，我们仍然可以通过调用 广播机制 来执行按元素操作
a=torch.arange(3).reshape((3,1))   #一列
#对于reshape这个函数来说，如果参数时一个整形，就是一堆数组；如果是（，），则代表一个元组
b=torch.arange(2).reshape((1,2))   #一行
a,b
a+b        #（3，1）把后面1的维度复制成两项变为3*2   （1，2）把前面1复制成3项变为3*2

X[-1],X[1:3]  #元素的访问  访问X最后一行 访问X第一行和第二行
X[1,2]=9   #指定索引来将元素写入矩阵
X[0:2,:]=12 #为多个元素赋值相同的元素  只需要索引所有元素，然后为它们赋值

#运行一些操作可能会导致为新结果分配内存
#内存析构，即销毁原来的变量，释放内存
before=id(Y)   #id类似C语言的指针
Y=Y+X    #Y=X+Y相当于X和Y加完又给了新创建的Y
id(Y)==before
#执行原地操作,对元素进行改写，地址不变
Z=torch.zeros_like(Y)
print('id(Z):',id(Z))
Z[:]=X+Y
print('id(Z):',id(Z))
#如果在后续计算中没有重复使用X，我们也可以使用X[:]=X+Y或X+=Y来减少操作的内存开销
before=id(X)
X+=Y   #  += 相当于有[:]的操作本质是赋值   而X=X+Y相当于X和Y加完又给了新创建的X
id(X)==before

#转换成numpy张量
A=X.numpy()
B=torch
