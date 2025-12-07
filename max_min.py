""" without use """
import json
def main():
    """ input """
    l_1 = json.loads(input())
    mem = len(l_1)
    avg = sum(l_1) / mem
    avg = round(avg,2)
    most = l_1[0]
    least = l_1[0]

    for i in l_1:
        if i > most:
            most = i

    for j in l_1:
        if j < least:
            least = j

    most = round(most,2)
    least = round(least,2)
    print(f"({most}, {least}, {avg})")



main()
