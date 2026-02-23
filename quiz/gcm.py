"""gcd without using gcd"""
def lcm(a,b):
    l1 = []
    if a == 0 or b == 0:
        return 0
    mini = min(a,b)
    for i in range(1,mini+1):
        if (a%i == 0) and (b%i == 0):
            l1.append(i)
    
    max_lcm = max(l1)
    return max_lcm

print(lcm(int(input()),int(input())))
