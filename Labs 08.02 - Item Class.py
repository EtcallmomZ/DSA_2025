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


def main():
    import json
    item_in = json.loads(input())
    Item = item(item_in["name"], item_in["price"], item_in["weight"])
    print(Item.get_name(), Item.get_price(), Item.get_weight(), sep='\n')

main()
