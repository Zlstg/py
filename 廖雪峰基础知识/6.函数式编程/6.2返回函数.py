#  返回函数
# 函数作为返回值
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
if __name__ == '__main__':
    print(calc_sum(10,20,30))

# 如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax= 0
        for n in args:
            ax = ax + n
        return ax
    return sum
if __name__ == '__main__':
    print(lazy_sum(10))
    x = lazy_sum(10)
    print(x == lazy_sum(10))
    print(x())

# 闭包
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
if __name__ == '__main__':
    print(count())
    x, y, z = count()
    print(x(), y(), z()) # 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
if __name__ == '__main__':
    print(count())
    x, y, z = count()
    print(x(), y(), z())

'''
练习
利用闭包返回一个计数器函数，每次调用它返回递增整数：
'''
def createCounter():
    x=0
    def counter():
        nonlocal x
        x+=1
        return x
    return counter
if __name__ == '__main__':
    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')