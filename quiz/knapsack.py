"""item class"""
from math import remainder


class Item:
    """Item class"""
    def __init__(self, name:str,price:int,weight:float):
        self.__name=name
        self.__price=price
        self.__weight=weight

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> int:
        return self.__price

    def get_weight(self) -> float:
        return self.__weight

    def get_cost(self) -> float:
        return self.__weight // self.__price


def knapsack(amount:float,itemList:list):
    print(f"Knapsack Size: {amount}")
    print("===============================")
    sored_items= sorted(itemList,key=lambda item: item.get_cost(),reverse=True)
    total = 0
    remainder_capacity = amount
    for item in sored_items:
        if item.get_weight() <= remainder_capacity:
            print(f"{item.get_name()} -> {item.get_weight()} kg -> {item.get_price()} THB")
            remainder_capacity -= item.get_weight()
    print(f"Total: {total} THB")


def main():
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(knapsack_capacity,items)
main()