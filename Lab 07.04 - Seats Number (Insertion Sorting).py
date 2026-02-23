import json
def intersection(l_1,last):
    comparison = 0
    for current in range(1,last+1):
        hold = l_1[current]
        walker = current-1
        while walker >= 0:
            comparison += 1

            hold_char , hold_num = hold[0],int(hold[1:])
            walker_char , walker_num = l_1[walker][0],int(l_1[walker][1:])


            if (hold_char < walker_char) or (hold_char == walker_char and hold_num < walker_num):
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