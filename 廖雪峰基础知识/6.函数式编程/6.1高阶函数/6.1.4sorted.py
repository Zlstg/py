#  sorted
# 排序算法 Python内置的sorted()
L = [36, 5, -12, 9, -21]
print(sorted(L))

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序 例如按绝对值大小排序：
print(sorted(L, key=abs))
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。对比原始的list和经过key=abs处理过的list
list = [36, 5, -12, 9, -21]
keys = [36, 5,  12, 9,  21]

# 字符串排序 对字符串排序，是按照ASCII的大小比较的
strL = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(strL))
# 忽略大小写 按照字符排序
print(sorted(strL, key=str.lower))
# 反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(strL, key=str.lower, reverse=True))

'''
练习
假设我们用一组tuple表示学生名字和成绩：
请用sorted()对上述列表分别按名字排序：
'''
L = [('Bob', 75), ('adam', 22), ('Bart', 66), ('lisa', 88)]
def by_name(t):
    # return t[0].lower()
    return  t[0].upper()
if __name__ == '__main__':
    L2 = sorted(L, key=by_name)
    print(L2)
'''
再按成绩从高到低排序：
'''
def by_score(t):
    return -t[1]

if __name__ == '__main__':
    L2 = sorted(L, key=by_score)
    print(L2)