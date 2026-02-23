"""lcm without using lcm"""
def lcm(a,b):
    l1 = []
    if a == 0 or b == 0:
        return 0
    mini = min(a,b)
    for i in range(1,mini+1):
        if (a%i == 0) and (b%i == 0):
            l1.append(i)
    
    max_lcm = max(l1)
    result = (a//max_lcm) * (b//max_lcm) * (max_lcm)
    return result

print(lcm(int(input()),int(input())))
