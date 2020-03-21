from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_sofar, max_profit = float('inf'), 0.0
    if prices is not None:
        for price in prices:
            min_sofar = min(price, min_sofar)
            max_profit = max(max_profit, price - min_sofar)

    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
