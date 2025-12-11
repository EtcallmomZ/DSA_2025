""" fibonacci """
def fibonnacci(n):
    """ input """
    if not n:
        return 0
    if n == 1:
        return 1

    return fibonnacci(n-1) + fibonnacci (n-2)


print(fibonnacci(int(input())))
