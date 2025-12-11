""" probstat """
def prob():
    """ input """
    l_1 = []
    for _ in range(4):
        i = int(input())
        l_1.append(i)

    l_1.sort()
    print(sum(l_1[1:]))
prob()
