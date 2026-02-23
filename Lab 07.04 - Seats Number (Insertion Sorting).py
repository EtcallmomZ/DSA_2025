import json
def intersection(l_1,last):
    comparison = 0
    for i in range(1,last+1):
        hold = l_1[i]
        walker = i-1
        while walker >= 0:
            comparison += 1
            if hold < l_1[walker]:
                l_1[walker+1] = l_1[walker]
                walker -= 1
            else:
                break
        
        l_1[walker + 1] = hold
        print(l_1)
    print(f"Comparison times: {comparison}")


def main():
    a = json.loads(input())
    b = int(input())
    intersection(a,b)
main()