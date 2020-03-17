#coding:utf-8
#   函数的参数
'''定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。对于函数的调用者来说，
只需要知道如何传递正确的参数，以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，调用者无需了解。

Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、
可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。
'''
#位置参数
#写一个计算x^2的函数
def power(x):
    return x * x
print(power(5))
print(power(15))
'''现在，如果我们要计算x3怎么办？可以再定义一个power3函数，但是如果要计算x4、x5……怎么办？
我们不可能定义无限多个函数。
'''
#可以把power(x)修改为power(x, n)，用来计算xn，说干就干：
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5, 2))
print(power(5, 3))

#默认参数
#新的power(x, n)函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数，
# 导致旧的代码因为缺少一个参数而无法正常调用：
#print(power(5))    TypeError: power() missing 1 required positional argument: 'n'v
#Python的错误信息很明确：调用函数power()缺少了一个位置参数n。
#这个时候，默认参数就排上用场了。由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2：
def power(x, n=2):    #设置n的默认值是2
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5))
print(power(5, 2))
#一年级小学生注册的函数，需要传入name和gender两个参数：
def enroll(name, gender):
    print('name:',name)
    print('gender:',gender)
#这样，调用enroll()函数只需要传入两个参数：
enroll('xiaohei', 'A')
#如果要继续传入年龄、城市等信息怎么办？这样会使得调用函数的复杂度大大增加。
#我们可以把年龄和城市设为默认参数：
def enroll(name, gender, age=8, city='nanjing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)
print(enroll('xiaohei','A'))
#只有与默认参数不符的学生才需要提供额外的信息：
print(enroll('xiaohei','A',city='suqian'))
#默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑
#先定义一个函数，传入一个list，添加一个END再返回：
def add_end(L=[]):
    L.append('END')
    return L
#正常调用时：
print(add_end([1,2,3]))
#使用默认参数调用时，一开始结果也是对的：
print(add_end())
#但是，再次调用add_end()时，结果就不对了：
print(add_end())
print(add_end())
#定义默认参数要牢记一点：默认参数必须指向不变对象！
#修改上面的例子，我们可以用None这个不变对象来实现：
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
#现在，无论调用多少次，都不会有问题：
print(add_end())
print(add_end())
'''为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，
这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，
同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。'''

#可变参数
'''在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。

要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，
我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：'''
def calc(numbers):
    sum=0
    for n in numbers:
        sum = sum+n*n
    return sum
#调用的时候，需要先组装出一个list或tuple：
print(calc([1,2,3]))
print(calc((1,3,5,7)))
'''如果利用可变参数，调用函数的方式可以简化成这样：
print(calc(1,2,3))
print(calc(1,3,5,7))'''
#把函数的参数改为可变参数：
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum+n*n
    return sum
print(calc(1,2,3))
print(calc(1,3,5,7))
#如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
nums = [1,2,3]
print(calc(nums[0],nums[1],nums[2]))
#这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，
# 把list或tuple的元素变成可变参数传进去：
print(calc(*nums))
#*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

#   关键字参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
#函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：
person('xiaohei',2)
#也可以传入任意个数的关键字参数：
person('xiaohua',2,city='suqian')
person('xiaohei',2,gender='M',job='eat')
#关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，
# 但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，
# 除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
#和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra={'city':'suqian','job':'eat'}
person('xiaohei',2,city=extra['city'],job=extra['job'])
#复杂的调用可以用简化的写法：
extra={'city':'suqian','job':'eat'}
person('xiaohei',2,**extra)
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

#   命名关键字参数
#对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
#仍以person()函数为例，我们希望检查是否有city和job参数：
def person(name,age,**kw):
    if 'city' in kw:    #有city参数
        pass
    if 'job'in kw:    #有job参数
        pass