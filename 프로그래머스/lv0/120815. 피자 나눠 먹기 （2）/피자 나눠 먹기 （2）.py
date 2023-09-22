def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(n):
    if(6>n):
        r=gcd(6,n)
    else:
        r=gcd(n,6)
    return n//r