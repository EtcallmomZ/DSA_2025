""" input """
def convert_key(data):
    """JSON"""
    return {int(k): v for k, v in data.items()}


def coinExchange(amount,coins):
    print(f"Amount: {amount}")
    vaule = sorted(coins.keys(),reverse=True)
    used_coins = {coin: 0 for coin in vaule} # ตั้งไว้ให้ไปเรียกค่าตอนลูป
    total = 0
    remainding_amount = amount

    for i in vaule:
        if remainding_amount <= 0:
            break
        need = remainding_amount // i
        use = min(need,coins[i])
        used_coins[i] = use
        remainding_amount -= (use * i)
        total += use

    if remainding_amount > 0:
        print("Coins are not enough.")
    else:
        print("Coin exchange result:")
        for i in vaule:
            print(f"  {i} baht = {used_coins[i]} coins")
        print(f"Number of coins: {total}")


def main():
    import json
    money = int(input())
    data = convert_key(json.loads(input()))
    coinExchange(money,data)
main()
