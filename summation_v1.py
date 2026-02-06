""" summation V1"""
def summation(n):
    """ what is it?? """
    summary = 0
    for i in range(n):
        summary += i
    summary += n
    return summary

print(summation(int(input())))
