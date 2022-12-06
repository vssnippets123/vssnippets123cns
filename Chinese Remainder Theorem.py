def inv(x, m):
    r1 = m
    r2 = x
    t1 = 0
    t2 = 1
    while(r2 > 0):
        q = r1 // r2
        r = r1 % r2
        t = t1 - q * t2
        r1 = r2
        r2 = r
        t1 = t2
        t2 = t

    if(t1 < 0):
        return t1 + m

    return t1


def findMinX(num, rem, k):
    prod = 1
    for i in range(0, k):
        prod = prod * rem[i]

    result = 0

    for i in range(0, k):
        pp = prod // rem[i]
        result = result + num[i] * inv(pp, rem[i]) * pp

    return result % prod


# x = num(mod rem)
n = int(input("Enter n: "))

num = list(map(int, input("Enter nums : ").strip().split()))[:n]
rem = list(map(int, input("Enter rems : ").strip().split()))[:n]

print("x is", findMinX(num, rem, n))
