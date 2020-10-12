# Selecting stock
"""
```Python
Q2: knapsack 

curr: [1, 2, 4, 6]; future: [5, 3, 5, 6]; saving: 30 => 6
"""

def max_profit(curr_price, future_price, saving):
    profit = [future_price[i] - curr_price[i] for i in range(len(curr_price))]
    return _max_profit(curr_price, profit, saving)

def _max_profit(price, profit, saving):
    total_stocks = len(price)
    # table[s][i] = max profit we can make for first i stocks (i.e. prices[:i]) with saving s
    # table[0][:] = 0
    # table[:][0] = 0 
    table = [[0] * (total_stocks + 1) for i in range(saving + 1)]
    # transion func:
    #   table[s][i] = max(table[s][i-1], table[s-prices[i]][i-1] + profit[i])
    for i in range(1, total_stocks + 1):
        for s in range(1, saving + 1):
      # current item's price is price[i-1], profit is profit[i-1]
            if s >= price[i-1]:
            # buy or not
                table[s][i] = max(table[s][i-1], table[s-price[i-1]][i-1] + profit[i-1])
            else:
                table[s][i] = table[s][i-1]
    print(table)
    ## debug
    # for r in table:
    #   print(r)
    return table[saving][total_stocks]

test_curr_price_1 = [1, 2, 4, 6]
test_future_price_1 = [5, 3, 5, 6]
test_saving_1 = 30
print(max_profit(test_curr_price_1, test_future_price_1, test_saving_1))
```
