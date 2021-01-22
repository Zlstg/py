#coding:utf-8
#输入用户年龄，根据年龄打印不同的内容，在Python程序中，用if语句实现：
age = 20
if age >= 18:
    print('you age is:',age,'\nadult')
else:
    print('you age is:',age,'\nteenager')
#------------------------------------------
age = 15
if age >= 18:
    print('you age is:',age,'\nadult')
else:
    print('you age is:',age,'\nteenager')
#elif是else if的缩写，完全可以有多个elif
age = 46
if age >= 60:
    print('you age is:',age,'old')
elif age >= 45:
    print('you age is:',age,'adult old')
elif age >= 18:
    print('you age is:',age,'adult')
else:
    print('you age is:',age,'baby')

#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
x = 0
if x:
    print(True)
else:
    print(False)

#用input()读取用户的输入,因为input()返回的数据类型是str，str不能直接和整数比较，
# 必须先把str转换成整数。int()函数来完成
'''
birth = input('birth:')
s = int(birth)
if s >2010:
    print('10后')
elif s >2000:
    print('00后')
elif s >1990:
    print('90后')
elif s >1980:
    print('80后')
else:
    print('you old')
'''
'''练习小明身高1.75，体重80.5kg。
请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''
height = 1.75
weight = 80.5
bmi = weight/height ** 2
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')



