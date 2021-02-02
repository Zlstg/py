# ---- 迭代器 ----
# 使用isinstance()判断一个对象是否是Iterable对象
from collections.abc import Iterable
print('list:',isinstance([],Iterable))
print('dict: ',isinstance({},Iterable))
print('str: ',isinstance('abc',Iterable))
print('生成器: ',isinstance([x for x in range(10)], Iterable))
print('generator: ',isinstance((x for x in range(10)), Iterable))
print('int: ',isinstance(100,Iterable))

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
from collections.abc import Iterator
print('-------------Iterator')
print('generator: ',isinstance((x for x in range(10)), Iterator))
print('list: ', isinstance([], Iterator))
print('dict: ', isinstance({}, Iterator))
print('str: ', isinstance('abc', Iterator))

# 要把 list duct str等Iterable变成Iterator可以使用iter()函数
print('---------------iter(),Iterator')
print('list: ',isinstance(iter([]),Iterator))
print('dict: ',isinstance(iter(()),Iterator))
print('str: ',isinstance(iter('anc'),Iterator))




# 小结
print('----------------小结')
for x in [1, 2, 3, 4, 5]:
    print(x)
print('完全等价于:')
it = iter([1, 2, 3, 4, 5])

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
