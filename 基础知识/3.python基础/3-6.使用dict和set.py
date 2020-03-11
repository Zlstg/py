#coding:utf-8
#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，
# 使用键-值（key-value）存储，具有极快的查找速度。
#用dict实现，只需要一个“名字”-“成绩”的对照表
d = {'xiaohei':100,'xiaohua':60,'zhula':65}
print(d['xiaohei'])
#数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
d['zhula'] = 61
print(d['zhula'])
#一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
d['zhula'] = 60.5
print(d['zhula'])
#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('zhula' in d)
#二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('zhul'))
print(d.get('zhul','空值'))
d['test'] = 80
print(d)
#要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('test')
print(d)
#dict的key必须是不可变对象

#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set([1,2,3])
print(s)
#重复元素在set中会被自动过滤
s = set([1,2,2,3,3])
print(s)
#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(4)
s.add(4)
s.add(5)
print(s)
#通过remove(key)方法可以删除元素：
s.remove(2)
print(s)
#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1,2,3])
s2 = set({3,4,5})
print(s1 & s2)    #s1和s2的交集
print(s1 | s2)    #s1和s2的并集

#不可变对象
#对于可变对象，比如list，对list进行操作，list内部的内容是会变化的
a = ['c','a','b']
a.sort()
print(a)
#而对于不可变对象，比如str，对str进行操作呢：
a = 'abc'
b = a.replace('a','A')
print(a,b)
