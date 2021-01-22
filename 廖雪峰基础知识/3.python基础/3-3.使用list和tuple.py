# coding:utf-8
# list是Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Miss', 'xiaoming', 'xiaohong']
print(classmates)
# 变量classmates就是一个list。
print('--- 用len()函数可以获得list元素的个数 ---')
print(len(classmates))
# 用索引来访问list中每一个位置的元素，记得索引是从0开始的：
print(classmates[0])
print(classmates[1])
print(classmates[2])
# 当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，
'''print(classmates[3])'''
print('--- 最后一个元素的索引是len(classmates) - 1 ---')
print(len(classmates) - 1)
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print(classmates[-1])
# 以此类推可以获取倒数第二个第三个
print(classmates[-2])
print(classmates[-3])
'''print(classmates[-4])'''
# list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append('xiaohei')
classmates.append('niaoniao')
print(classmates)
# 也可以把元素插入到指定的位置，比如索引号为1的位置：索引号从0开始
classmates.insert(1, 'ergou')
print(classmates)
classmates.insert(2, 'test')
print(classmates)
# 要删除list末尾的元素，用pop()方法：
print(classmates.pop())
print(classmates)
classmates.insert(0, 'xiaohei')
print(classmates)
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(2)
print(classmates)
# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
# list里面的元素的数据类型也可以不同
classmates[1] = '小花'
classmates[0] = '小黑'
classmates[2] = 123
print(classmates)
# list元素也可以是另一个list
a = ['python', 'java', ['php', 'js', 'css'], 'c++']
print(len(a))
# a只有4个元素，也可以拆开写
b = ['php', 'js', 'css']
c = ['python', 'java', 'c++', b]
print(c)
# 要拿到'php'可以写b[0]或者c[3][0]，
# 因此s可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到。
print(b[0])
print(c[3][0])
# 如果一个list中一个元素也没有，就是一个空的list，它的长度为0：
d = []
print(len(d))


#tuple
#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
classes = ('小黑','xiaohua',123)
print(classes)
#现在，classes这个tuple不能变了，它也没有append()，insert()这样的方法。
# 其他获取元素的方法和list是一样的，你可以正常地使用classes[0]，classes[-1]，
# 但不能赋值成另外的元素。
print(classes[0])
print(classes[1])
print(classes[2])
#因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
e = (1,2)
print(e)
e = ()
print(e)
e = (1)
print(e)
e = (1,)
print(e)
#tuple和list可以混合使用
t = ('a','b',['c','d'],'e')
t[2][0] = 'x'
t[2][1] = 'y'
print(t)
