import json
def selection_sort(l1,last):
    current = 0
    compare_time =  0
    for current in range(current,last):
        smallest = current
        walker = current +1
        while walker <= last:
            compare_time += 1

            char_walker,num_walker = l1[walker][0] , int(l1[walker][1:])
            char_smallest,num_smallest = l1[smallest][0] , int(l1[smallest][1:])

            
            if char_walker < char_smallest or (char_walker == char_smallest and num_walker < num_smallest):
                smallest = walker
            walker += 1
        
        l1[current],l1[smallest] = l1[smallest],l1[current]

        print(l1)
    print(f"Comparison times: {compare_time}")
    
def main():
    a = json.loads(input())
    b = int(input())
    selection_sort(a,b)
main()