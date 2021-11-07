import sys
from typing import * 
def stock_profit(prices: List[int])->int:
    max_profit = -100
    min_price = sys.maxsize
    for var in prices:
        if min_price > var:
            min_price = var
        if max_profit < var - min_price:
            max_profit = var- min_price
    return max_profit

prices = [7,5,3,6,4,10,8,9,16]
print(f'max profit:: {stock_profit(prices)}')