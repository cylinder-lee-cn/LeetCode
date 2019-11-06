"""
质数（素数）：埃氏筛法

构造一个大小为n的列表，初值都是1，每发现一个素数，我们把所有它的倍数都置为0，直到发现下一个为1的数为素数。

一个数要么是质数，要么是一系列质数的积，也就是分解质因数

def eratosthenes(n):
    IsPrime = [True] * (n + 1)
    IsPrime[1] = False #1不为素数
    for i in range(2, int(n ** 0.5) + 1):
        if IsPrime[i]:
            for j in range(i * i, n + 1, i):
                IsPrime[j] = False
    return {x for x in range(2, n + 1) if IsPrime[x]}
"""


def prime_eratosthenes(n):
    flag = [1] * (n + 2)  # 用数组的index代表对应的数
    p = 2  # 第一个质数，1不是质数

    while (p < n):
        print(p)
        for i in range(p * 2, n + 1, p):  # 从p这个数的1倍开始，每次递进p
            flag[i] = 0
        while 1:
            p = p + 1  # 递增这个数
            if (flag[p] == 1):  # 如果这个数字没有被标记为0，就跳出当前while，进行外部的大循环
                break
    return flag


# pp = prime_eratosthenes(100)


def is_prime(n):
    if (n <= 1):
        return False
    if (n % 2 == 0):
        return (n == 2)
    if (n % 3 == 0):
        return (n == 3)
    if (n % 5 == 0):
        return (n == 5)
    for p in range(7, (int(n**0.5) + 1), 2):  # 只考虑奇数为因子的情况
        print(p)
        if (n % p == 0):
            return False
    return True


# print(is_prime(1))
"""
        ans = 0
        judge = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0,
                1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0]
        for i in range(L, R + 1):
            if judge[bin(i).count('1')]:
                ans += 1
            # ans=ans+judge[i]
        return ans
"""
# TODO: Euler 筛法的继续完善。
"""
欧拉筛选法：Euler筛法（Sieve of Euler）

"""


def prime_euler(n):
    ps = [2]  # 第一个质数
    for i in range(3, n, 2):  # 循环从3开始，只需要取奇数
        flag = True
        for j in ps:
            if (i % j == 0):  # 待判断的数字如果能被任意一个质数整除，就一定是合数
                flag = False
                break
        if flag:
            ps.append(i)
            print(i)
    print(ps)


prime_euler(1000)
