""" fibonacci """
def fibonnacci(n):
    """ input """
    if not n:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnacci(n-1) + fibonnacci (n-2)


print(fibonnacci(int(input())))
