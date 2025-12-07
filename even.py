""" even or not """
def is_even(k):
    """ input """
    if k & 1 == 0:
        return True
    return False

print(is_even(int(input())))

