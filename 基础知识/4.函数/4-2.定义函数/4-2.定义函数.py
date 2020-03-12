#coding:utf-8
#定义函数
#定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:
#然后，在缩进块中编写函数体，函数的返回值用return语句返回
#自定义一个求绝对值的my_abs函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-80))
print(my_abs(12.68))
#已经把abs()的函数定义保存为dy_abs.py文件,可以在该文件的当前目录下启动Python解释器
#用from abstest import dyabs来导入abs()函数，注意abstest是文件名（不含.py扩展名）：
from abstest import dyabs
print(dyabs(-99))
#如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass
#pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，
#比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
#pass还可以用在其他语句里，比如：
age = 14
if age >= 18:
    pass

#    参数检查
#调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：
'''    my_abs(1,2)
TypeError: my_abs() takes 1 positional argument but 2 were given'''
#但是如果参数类型不对，Python解释器就无法帮我们检查。试试my_abs和内置函数abs的差别：
'''my_abs('A')    TypeError: '>=' not supported between instances of 'str' and 'int'
abs('A')    TypeError: bad operand type for abs(): 'str' '''
#当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查，会导致if语句出错，
# 出错信息和abs不一样。所以，这个函数定义不够完善。
#修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。
# 数据类型检查可以用内置函数isinstance()实现：
def my_abs(x):
    if not isinstance(x, (int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
'''my_abs('A')
raise TypeError('bad operand type')
TypeError: bad operand type'''

 #返回多个值
 #在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的坐标：
import math
def move(x,y,step,angle=0):
    nx = x+step*math.cos(angle)
    ny = y-step*math.sin(angle)
    return nx, ny
#可以同时获得返回值：
x, y = move(100,100,60,math.pi / 6)
print(x, y)
#可以同时获得返回值：
r = move(100,100,60,math.pi / 6)
print(r)

#练习
#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0 的两个解。
#一元二次方程的求根公式为：
'''
x= (-b+√￣（b^2-4ac）)/2a
计算平方跟可以调用math.sqrt()函数：
上文 以引用import math
print(math.sqrt(2))    #1.4142135623730951 '''''
def quadratic(a, b, c):
    x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
    return x1,x2
print('quadratic(2,3,1)=',quadratic(2,3,1))
print('quadratic(1,3,-4)=',quadratic(1,3,-4))
if quadratic(2,3,1)!=(-0.5,-1.0):
    print('第一组测试失败')
elif quadratic(1,3,-4)!=(1.0,-4.0):
    print('第二组测试失败')
else:
    print('测试成功')


