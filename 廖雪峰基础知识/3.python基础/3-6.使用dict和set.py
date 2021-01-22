#dict
print('从dict中取值')
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])

print('\n\n\n------dict塞值')
print(d)
d['xiaoming'] = 100
print(d)

print('\n\n\n--------修改key对应的value')
print(d)
d['xiaoming'] = 99
print(d)

print('\n\n\n-------如果key不存在则报错')
# print(d['xiaohong'])
print('两种方法判断key是否存在，True存在 False不存在')
print(d)
print('通过 in 判断 xiaoming：','xiaoming' in d)
print('xiaohong' in d)
print('通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value')
print(d.get('xiaoming1'))
print(d.get('xiaoming1','不存在'))


print('\n\n\n-------------------使用pop()删除key对应value也删除')
print(d)
print(d.pop('Bob'))
print(d)

print('\n\n\n--------------set 一组key的组合')
s = set([1,2,3,4])
print(s)
#没有重复的key
s = set([1,1,2,2,3,4])
print(s)
#通过add(key)可以添加元素到set中
print(s)
s.add(9)
s.add(1)
print(s)
s.remove(1)
print(s)

#set可以做数学意义上的交集、并集等操作
s1 = set([1,2,3])
s2 = set([2,3,4])
print('s1和s2的交集：',s1 & s2)
print('s1和s2的并集：',s1 | s2)
