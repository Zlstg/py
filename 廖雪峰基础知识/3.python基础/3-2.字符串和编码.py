#coding:utf-8
print('包含中文的str')
#两个字节可以表示最大的整数是65535,4个字节可以表示最大的整数是5294967295
print('order()函数获取字符的整数表示，chr()函数把编码转换为对应的字符')
print('字符\'A\'的编码是:',ord('A'))
#   65
print('字符\'中\'的编码是:',ord('中'))
#   20013
print('将编码 66 转换为字符：',chr(66))
#   B
print('将编码 225991 转换为字符：',chr(25991))
#   文
print(r'将整数编码\u4e2d\u6587转换成字符：','\u4e2d\u6587')

print('对bytes类型的数据用带b前缀的单引号或双引号表示')
x = b'ABC'
print(x)
print('--- 前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节 ---')
'''
>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
>>> '中文'.encode('ascii')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
#纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。
#含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
'''

#从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
'''
>>> b'ABC'.decode('ascii')
'ABC'
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
'''

#如果bytes中包含无法解码的字节，decode()方法会报错：
'''
>>>  b'\xe4\xb8\xad\xff'.decode('utf-8')
  File "<stdin>", line 1
    b'\xe4\xb8\xad\xff'.decode('utf-8')
    ^
IndentationError: unexpected indent
'''

#如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
'''
>>> b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
'中'
'''

print('--- 要计算str包含多少个字符，可以用len()函数 ---')

print(len('ABC'))
# 3
print(len('中文'))
# 2

print('--- len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数 ---')
print(len(b'ABC'))
# 3
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
# 6
print(len('中文'.encode('utf-8')))
# 6
print(len('ABC'.encode('ascii')))
# 3

#格式化
#在Python中，采用的格式化方式和C语言是一致的，用%实现

print('Hello,%s' %'word,,,,')
# 'Hello,word'
print('Hi, %s, you have $%d.' % ('Miss', 10000000))
# 'Hi, Miss, you have $10000000.'

'''
常见占位符有
%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数
'''
print('%5d-%02d' % (3,1))
print('%.3f' % 3.1415926)

#%s永远起作用，它会把任何数据类型转换为字符串：
'''
>>> 'Age:%s. Miss:%s' % (25,True)
'Age:25. Miss:True'
'''

#字符串里面的%是一个普通字符,用%%表示%
'''
>>> '7 is 7,is\'t %s%%' % (7)
"7 is 7,is't 7%"
'''

#另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，
# 不过这种方式写起来比%要麻烦得多：
'''
>>> 'hello, {0},成绩提升了 {1:.1f}%'.format('小明',17.156)
'hello, 小明,成绩提升了 17.2%'
'''

#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，
# 并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1 = 72
s2 = 85
z = (s2-s1)/s1*1e2
print('小明的成绩从去年的%d分，提升到了今年的%d分，比去年提升了%.1f%%' % (s1,s2,z))
print('小明的成绩从去年的{0}分，提升到了今天的{1}分，比去年提上了{2:.1f}%'.format(s1,s2,z))