import json
def bubble_sort(l1,last):
    current = 0
    compare_time = 0
    sorted_bool = False
    while current <= last and sorted_bool is False:
        walker = last
        sorted_bool = True
        while walker > current:
            compare_time += 1
            if l1[walker] < l1[walker -1]:
                sorted_bool = False
                l1[walker],l1[walker-1] = l1[walker-1],l1[walker]
            walker -= 1
        current += 1
        print(l1)
    print(f"Comparison times: {compare_time}")

def main():
    a = json.loads(input())
    b = int(input())
    bubble_sort(a,b)
main()
