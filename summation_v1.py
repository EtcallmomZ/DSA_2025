""" summation V1"""
def summation(n):
    """ what is it?? """
    summary = 0
    for _ in range(1,n+1):
        summary += n
    return summary

print(summation(int(input())))
