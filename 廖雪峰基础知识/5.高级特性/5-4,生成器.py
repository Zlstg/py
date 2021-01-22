#    生成器：generator
# 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)    # g是一个generator
for n in g:
    print(n)

# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1
    return 'done'
'''
赋值语句：
a, b = b, a + b

相当于：
t = (b, a + b) # t是一个tuple
a = t[0]
b = t[1]
'''
if __name__ == "__main__":
    print('---------------------斐波拉契数列')
    print(fib(6))

# generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


if __name__ == "__main__":
    print('---------------------斐波拉契数列')
    print(fib(6))

# yield关键字
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

if __name__ == '__main__':
    print('----------------yield 关键字')
    o = odd()
    print(next(o))
    print(next(o))
    print(next(o))

    print('----------generator')
    for f in fib(6):
        print(f)
    # 获取generator函数的return
    g = fib(6)
    while True:
        try:
            x = next(g)
            print('g: ',x)
        except StopIteration as e:
            print('Generator return value:',e.value)
            break


'''
练习
杨辉三角定义如下：
          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list：
'''
def triangles():
    n=[1]
    while True:
        yield n
        n=[1]+[n[i]+n[i+1] for i in range(len(n)-1)]+[1]

if __name__ == '__main__':
    n = 0
    results = []
    for t in triangles():
        results.append(t)
        n = n + 1
        if n == 10:
            break

    for t in results:
        print(t)

    if results == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    ]:
        print('测试通过!')
    else:
        print('测试失败!')


