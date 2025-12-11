""" input """
def gcd(a,b):
    """ input """
    if b == 0:
        return a
    return gcd(b,a%b)

x = int(input())
y = int(input())
print(gcd(x,y))
