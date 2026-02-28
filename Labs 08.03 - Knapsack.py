class item:
    def __init__(self,name:str,price:int,weight:float):
        # "self'.__'name"  is set a attribute to private
        self.__name = name 
        self.__price = price
        self.__weight = weight

    def get_name(self) -> str: # "-> str" means return str
        return self.__name

    def get_price(self) -> int:
        return self.__price

    def get_weight(self) -> float:
        return self.__weight
    
    def get_cost(self) -> float:
        return self.__price / self.__weight
    
def knapsack(amount : float ,itemList: list):
    print(f"Knapsack Size: {amount} kg")
    print("===============================")

    sorted_item = sorted(itemList, key=lambda x: x.get_cost(),reverse=True)
    total = 0
    remaining_capacity = amount

    for i in sorted_item:
        if i.get_weight() <= remaining_capacity:
            print(f"{i.get_name()} -> {i.get_weight()} kg -> {i.get_price()} THB")
            total += i.get_price()
            remaining_capacity -= i.get_weight()

    print(f"Total: {total} THB")


def main():
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(knapsack_capacity,items)
main()
