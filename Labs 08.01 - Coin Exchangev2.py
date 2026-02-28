""" input """
def convert_key(data):
    """JSON"""
    return {int(k): v for k, v in data.items()}


def coinExchange(amount,coins):
    print(f"Amount: {amount}")
    data = convert_key(coins)
    used_coins = {coin: 0 for coin in data} # ตั้งค่าให้เป็น 0
    total = 0
    remainding_amount = amount

    for i in data:
        if remainding_amount <= 0:
            break
        need = remainding_amount // i
        use = min(need,data[i])
        used_coins[i] = use
        remainding_amount -= (use * i)
        total += use

    if remainding_amount > 0:
        print("Coins are not enough.")
    else:
        print("Coin exchange result:")
        for i in data:
            print(f"  {i} baht = {used_coins[i]} coins")
        print(f"Number of coins: {total}")


def main():
    import json
    money = int(input())
    data = json.loads(input())
    coinExchange(money,data)
main()
