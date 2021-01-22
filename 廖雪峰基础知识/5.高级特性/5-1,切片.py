L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取前三个元素
print("第一种方法：",[L[0], L[1], L[2]])

r = []
n = 3
for i in range(n):
    r.append(L[i])
print('第二种方法：',r)

print('第三种方法: ',L[:3])

# 取倒数第一个元素
print(L[-1:])

#新增一个0-99的数列
L = list(range(100))
print(L[:])
#取前十个数
print(L[:10])
#取后十个数
print(L[-10:])
#取前11-20
print(L[10:20])
#取前十个数，并且每两个取一个
print(L[:10:2])
#所有数每五个取
print(L[::5])


# tuple
L = (0, 1, 2, 3, 4, 5)
print(L[:3])

#字符串
L = 'ABCDEFG'
print(L[:3])


# 练习
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def  trim(s):
    s = s.strip()
    return s



if __name__ == "__main__":
    if trim('hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello') != 'hello':
        print('测试失败!')
    elif trim('  hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello  world  ') != 'hello  world':
        print('测试失败!')
    elif trim('') != '':
        print('测试失败!')
    elif trim('    ') != '':
        print('测试失败!')
    else:
        print('测试成功!')
