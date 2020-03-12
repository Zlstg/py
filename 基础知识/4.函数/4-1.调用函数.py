#Python内置了很多有用的函数，我们可以直接调用。
#调用abs函数：
print(abs(100))
print(abs(-80))
print(abs(16.23))
print(abs(-26.12))
#如果传入的参数数量不对，会报TypeError的错误，并且Python会明确地告诉你：
'''
abs(1, 2) # abs()有且仅有1个参数，但给出了两个
'''
#如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误
#并且给出错误信息：str是错误的参数类型：
'''abs('a')'''
#函数max()可以接收任意多个参数，并返回最大的那个：
print(max(1,5,78,95,1,6))
print(max(5,5.5,-3,2))
#Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数：
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))
#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs
print(a(-1))    #通过变量a调用abs()绝对值函数

#练习
#利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
i = int(input('Enter your number:'))
n = str(hex(i))
print(n)
#简洁写法
print(str(hex(int(input('Enter your number:')))))