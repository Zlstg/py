# python内建了map()和reduce()函数
# 有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现
'''
            f(x) = x * x

                  │
                  │
  ┌───┬───┬───┬───┼───┬───┬───┬───┐
  │   │   │   │   │   │   │   │   │
  ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼

[ 1   2   3   4   5   6   7   8   9 ]

  │   │   │   │   │   │   │   │   │
  │   │   │   │   │   │   │   │   │
  ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼

[ 1   4   9  16  25  36  49  64  81 ]

'''

def f(x):
    return x * x
if __name__ == '__main__':
    r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(r)
    print(list(r))

    #不需要map函数 利用循环计算出结果
    L = []
    for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        L.append(f(n))
    print(L)

# 利用map() 把list中所有整数转化成str
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))



#  reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 对一个序列求和
from functools import reduce
def add(x, y):
    return x + y
if __name__ == '__main__':
    print(reduce(add, [1, 3, 5, 7, 9]))
# 求和运算可以直接用Python内建函数sum()，没必要动用reduce
print(sum([1, 3, 5, 7, 9]))

# 把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x, y):
    return x * 10 + y
if __name__ == '__main__':
    print(reduce(fn, [1, 3, 5, 7, 9]))

# 把str转换为int
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
if __name__ == '__main__':
    print(reduce(fn, map(char2num, '13579')))
# 整理成str2int
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 * y
    def chae2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
# 用lambda函数进一步简化
def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

'''
练习
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
'''
def normalize(name):
    return name.capitalize()
if __name__ == '__main__':
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    if L2 == ['Adam', 'Lisa', 'Bart']:
        print('---------练习通过')
    else:
        print('----------练习不通过')

'''
Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
'''
def prod(L):
    def f(x, y):
        return x * y
    return reduce(f, L)
if __name__ == '__main__':
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('---------练习通过')
    else:
        print('----------练习不通过')


'''
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
'''
CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}
def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)



if __name__ == '__main__':
    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('---------练习通过')
    else:
        print('----------练习不通过')