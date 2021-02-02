#  高阶函数

# 变量可以指向函数
# 绝对值函数 abs()
print(abs(-10))

# abs是函数本身
print(abs)

# 也可以吧函数结果赋值给变量
x = abs(-10)
print(x)
# 函数本身赋值给变量 , 变量可以指向函数
x = abs
print(x)

print('------变量指向函数，通过变量来调用函数')
f = abs
print(f(-10))


#  函数名也是变量
# abs = 10
# print(abs(-10))

#  传入函数
# 定义一个最简单的高阶函数
def add(x, y, f):
    return f(x) + f(y)
if __name__ == '__main__':
    print(add(-5, 6, abs))