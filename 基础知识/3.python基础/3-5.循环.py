#coding:utf-8
#   循环
#Python的循环有两种，
# 一种是for...in循环，依次把list或tuple中的每个元素迭代出来
names = ['xiaohei','xiaohua','zhula']
for name in names:
    print(name)    #会依次打印出names的每个元素
#所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。
#计算1-10的整数之和，可以用一个sum变量做累加
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)
#Python提供一个range()函数，可以生成一个整数序列
#再通过list()函数可以转换为list
print(list(range(11)))    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#这样就可以计算1-100的整数之和
sum = 0
for x in range(101):
    sum = sum + x
print(sum)    #5050
#第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
# 计算100以内所有奇数之和，可以用while循环实现：
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

#练习，利用循环依次对list中的每个名字打印出Hello, xxx!：
l = ['xiaohei','xiaohong','xiaohua']
for x in l:
    print('Hello,',x,'!')

#在循环中，break语句可以提前退出循环
'''
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')
'''
n = 1
while n <= 100:
    if n > 10:    # 当n = 11时，条件满足，执行break语句
        break    # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
#循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环
'''
n = 0
while n < 10:
    n = n + 1
    print(n)
'''
#只打印奇数，用continue语句跳过某些循环：
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:    #如果n是偶数 ，执行continue语句
        continue    #continue语句会直接机修下一轮循环后续的print语句不会执行
    print(n)



