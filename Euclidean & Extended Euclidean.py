def gcd(A, M):
    if A == 0:
        return M
    return gcd(M % A, A)


def Extended(m, x):
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


m = int(input("Enter M: "))
a = int(input("Enter A: "))

# A * X = 1 mod M
gcd_am = gcd(a, m)
inverse = Extended(m, a)
print("GCD = %d" % (gcd_am))
print("Multiplicative modular inverse - %d" % (inverse))
