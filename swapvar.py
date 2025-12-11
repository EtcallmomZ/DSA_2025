""" swapvar """
def swapvar():
    """ input """
    def convert_string_to_tuples(text_in):
        values = text_in.strip('()').split(', ')
        return tuple(map(float, values))

    data = convert_string_to_tuples(input())
    a = data[0]
    b = data[1]
    result = (b,a)
    print(result)
swapvar()
