#非零 非空字符串、list 就判断为True 否则 False
x = ''
i = 0
l = []

if x:
    print(True)
else:
    print('空字符串', False)
if i:
    print(True)
else:
    print('数值为0', False)
if l:
    print(True)
else:
    print('空list', False)



#for 循环
print('\n\n\n---------------for 循环')
names = ['哈士奇','边牧','拉布拉多','马犬']
for name in names:
    print(name)

print('\n\n\n使用for循环计算1-10的和')
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum += x
print(sum)

print('\n\n\n计算1-100的和。使用range()函数生成一个整数序列，再通过list()转化成list')
print(list(range(10)))

sum = 0
for x in list(range(101)):
    sum += x
print(sum)

#while 循环
print('\n\n\n---------------while 循环')
print('100以内奇数之和')
sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)

print('\n\n\n-------------break')
n = 0
while n < 10:
    n += 1
    if n > 3:
        break
    print(n)

print('\n\n\n---------------continue')
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)