from collections import defaultdict

# Count coins of each type


def count_coins(amount, coin, counter):
    while(amount >= coin):
        counter += 1
        amount = amount - coin
    return amount, counter


def main():
    coins = [25, 10, 5, 1]
    counters = [0] * len(coins)
    by_coin = defaultdict(int)
    amount = input("Enter amount in dollars: ")
    # Convert dollars to pennies
    amount = float(amount) * 100
    for coin, counter in zip(coins, counters):
        amount, counter = count_coins(amount, coin, counter)
        by_coin[coin] = counter
    print("Quarters: {0:d}, dimes: {1:d}, nickels: {2:d} and pennies: {3:d}."
          .format(*by_coin.values()))
    print("Total number of coins owed: {0:d}.".format(sum(by_coin.values())))


if __name__ == "__main__":
    main()
