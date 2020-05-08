# print absolute value of an integer:
a = 66
if a >= 0:
    print(a)
else:
    print(a+1)


a = -66
if a>= 0:
    print(a)
else:
    print(a-1)

print(-1.23e6)
print(12.3e-5)
print("i'm ok")
print('i\'m ok')
print("are you 'ok',\nyes i'm \"ok\"")
print('\\\n\\')

#如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，
# Python还允许用r''表示''内部的字符串默认不转义，
print('\\\t\\')
print(r'\\\t\\')

#如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，
# Python允许用'''...'''的格式表示多行内容，
print('line1\nline2\nline3')
print('''line1
line2
line3''')

#多行字符串'''...'''还可以在前面加上r使用
print(r'''hello,
world''')

#布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False，
# 在Python中，可以直接用True、False表示布尔值（请注意大小写），也可以通过布尔运算计算出来
print(3 > 2)
# True
print(3 > 5)
# False
#布尔值可以用and、or和not运算。
#and运算是与运算，只有所有都为True，and运算结果才是True：
print('-----and 与运算-----')
print(True and True)
# True
print(True and False)
# False
print(False and False)
# False
print(5 > 3 and 3 > 1)
# True
#or运算是或运算，只要其中有一个为True，or运算结果就是True：
print('-----or 或运算-----')
print(True or True)
# True
print(True or False)
# True
print(False or False)
# False
print(5 > 3 or 1 > 3)
# True
#not运算是非运算，它是一个单目运算符，把True变成False，False变成True：
print('-----not 非运算-----')
print(not True)
# False
print(not False)
# True
print(not 1 > 2)
# True
#布尔值经常用在条件判断中
print('--- 条件判断 ---')
age = 17
if age >= 18:
    print('adult')
else:
    print('teenager')
#空值用None标识，None不等于0
print('---空值用 None 表示，None不表示为0---')
print(None)

#变量
print('--- 变量 ---')
a = 1
print(a)

t_007 = 'T007'
print(t_007)

Answer = True
print(Answer)

print('--- 赋值语句的等号不等同于数学的等号 ---')
x = 10
x = x + 2
print(x)

#除法
print('--- 除法 ---')
x = 10 / 3
print(x)    #结果为浮点数
x = 10 / 2
print(x)    #整除的结果还是浮点数
print('--- 地板除 两个整数除法结果时整数 ---')
x = 10 // 3
print('10 // 3 =',x)
print('--- 余数运算，两个整数相除的余数 ---')
x = 10 % 3
print('10 % 3 =',x)