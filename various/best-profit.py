from itertools import combinations


def calc_profit_with_comb(prices: list) -> float:
    return max(sell - buy for buy, sell in combinations(prices, 2))


def calc_profit_with_max_min(prices: list) -> int:
    min_price = prices[0]
    max_price = 0
    for price in prices[1:]:
        min_price = min(min_price, price)
        max_price = max(price - min_price, max_price)
        # print(f'Price: {price}, min: {min_price}, max: {max_price}')
    return max_price


if __name__ == '__main__':
    prices = [5539, 1224, 4829, 2553, 1004, 2550, 5734, 6159, 3923, 445, 7224, 4404, 1187, 129]
    funcs = [calc_profit_with_comb, calc_profit_with_max_min]
    for func in funcs:
        print(f'Display maximun profit with {func.__name__}: {func(prices)}')
