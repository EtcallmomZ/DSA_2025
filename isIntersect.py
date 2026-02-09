import json
def intersect(a,b,c):
    """ true or false """
    return bool(set(a) & set(b) & set(c))

l1 = json.loads(input())
l2 = json.loads(input())
l3 = json.loads(input())
print(intersect(l1,l2,l3))
