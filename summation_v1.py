""" summation V1"""
def summation(n):
    """ what is it?? """
    summary = 0
    for _ in range(n):
        summary += n
    return summary

print(summation(int(input())))
