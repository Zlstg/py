#    dict 迭代
d = {'a': 1, 'b': 2, 'c': 3}
#dict默认迭代key
for key in d:
    print(key)
#dict迭代value
for value in d.values():
    print(value)
#dict同时迭代k v
for k, v in d.items():
    print(k ,v)

#   字符串迭代
for x in 'abc':
    print(x)

#   判断一个对象是可迭代对象
from collections import Iterable
print(isinstance('abc', Iterable))  # 判断str是否可迭代
print(isinstance([1,2,3], Iterable))    # list是否可迭代
print(isinstance(123, Iterable))    # 整数是否可迭代

# 如果要对list实现类似Java那样的下标循环 Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)

# for 循环同时引用两个变量
for x, y in ((1, 1), (2, 2), (3, 3)):
    print(x, y)

print('\n\n\n\n\n\n\n练习')
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    min = L and L[0] or None
    max = L and L[0] or None
    for x in L:
        min = min > x and x or min
        max = max < x and x or max
    return (min, max)


if __name__ == '__main__':
    if findMinAndMax([]) != (None, None):
        print('测试失败!')
    elif findMinAndMax([7]) != (7, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')