# 1.素数练习：
#     1,写一个函数isprime(x) 判断x是否为素数，如果是素数返回True
#     否则返回false
#     print(isprime(3))   #True 
#     2.写一个函数prime_m2n(m,n)返回从m开始，到n结束
#     范围内的素数，返回这些素数的列表，并打印（注：不包含n）
#     如：
#         L = prime_m2n(10,20)
#         print(L) #[11,13,17,19]
#     3.写一个函数primes(n)返回指定范围内的全部素数（不包含n）
#     的列表
#     如：   
#     L = primes(10)
#     print(L)    #[2,3,5,7]
#     1>计算100以内的全部素数的和
#     2>计算100～200之间全部素数的和
def isprime(x):
    if x < 2:
        return False
    for y in range(2,x):
        if x % y == 0:
            return False
    else:
        return True
print(isprime(1))
# def prime_m2n(m,n):
#     l = []
#     for x in range(m,n):
#         if isprime(x):
#             l.append(x)
#     return l
def prime_m2n(m,n):
    l = []
    for x in range(m,n):
        if x < 2:
            continue
        for y in range(2,x):
            if x % y == 0:
                break
        else:
            l.append(x)
    return l
print(prime_m2n(-5,20))
# def primes(n,m=0):
#     if m == 0:
#         l = prime_m2n(0,n)
#         return l
#     else:
#         l = prime_m2n(n,m)
#         return l
def primes(n,m=None):
    l = []
    if m == None:
        m,n = n,0 
    for x in range(n,m):
        if x < 2:
            continue
        for y in range(2,x):
            if x % y == 0:
                break
        else:
            l.append(x)
    return l
print('100以内的全部素数的和{},\n100～200之间全部素数的和{}\
# '.format(primes(100),primes(100,200)))