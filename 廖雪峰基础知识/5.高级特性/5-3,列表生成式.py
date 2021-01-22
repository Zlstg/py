# 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(1, 11)))

# 生成[1x1, 2x2, 3x3, ..., 10x10]
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)
# 使用列表生成式
print([x * x for x in range(1, 11)])
# 列表生成式仅偶数的平方
print([x * x for x in range(1, 11) if x % 2 == 0])
# 两层循环，生成全排列
print([x + y for x in 'ABC' for y in 'abc'])


# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os
print([d for d in os.listdir()])    # os.listdir可以列出文件和目录

#for循环同时迭代两个变量,使用dict的items()可以同时迭代key和value
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)
# 所以列表生成也可以使用两个变量
print([k+'=='+v for k, v in d.items()])


# 把一个list中所有字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])



#  if ... else
# for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else。
# 以下代码正常输出偶数：
print([x for x in range(1, 11) if x % 2 == 0])
# for前面加上if
print([x if x%2==0 else -x for x in range(1, 11)])


# 练习
# 修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]


if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')