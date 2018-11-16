# 1.写程序算出1~20的阶乘的和
# 1!+2!+3!+...+20!
def factorial(n):
    sum = 1
    for x in range(1,n+1):
        sum *= x
    return sum
print(sum(map(factorial,range(1,21))))