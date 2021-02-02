# Python内建的filter()函数用于过滤序列。
# filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# 在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

# 把一个序列中的空字符删除
def not_empty(s):
    return s and s.strip()
if __name__ == '__main__':
    print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

'''
用filter求素数
计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
首先，列出从2开始的所有自然数，构造一个序列：
2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
不断筛下去，就可以得到所有的素数。
用Python来实现这个算法，可以先构造一个从3开始的奇数序列：
'''
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
if __name__ == '__main__':
    print(_odd_iter())

def _not_dicisible(n):
    return lambda x : x % n > 0
def primes():
    yield 2
    it = _odd_iter() # 处室序列
    while True:
        n = next(it) # 返回序列第一个数
        yield n
        it = filter(_not_dicisible(n), it) # 构造新序列
if __name__ == '__main__':
    for n in primes():
        if n < 20:
            print(n)
        else:
            break



'''
练习
回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
'''

def is_palindrome(s):
    s = str(s)
    return s == s[::-1]

if __name__ == '__main__':
    output = filter(is_palindrome, range(1, 1000))
    print('1~1000:', list(output))
    if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99,
                                                      101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
        print('测试成功!')
    else:
        print('测试失败!')