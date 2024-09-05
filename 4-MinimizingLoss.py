def minimize_loss(prices):
    min_loss = float('inf') 
    buy_year = sell_year = -1

    
    for buy in range(len(prices)):
        for sell in range(buy + 1, len(prices)):
            loss = prices[buy] - prices[sell]
            
            if loss > 0 and loss < min_loss:
                min_loss = loss
                buy_year = buy + 1  #(because years start at 1)
                sell_year = sell + 1
    
    
    return buy_year, sell_year, min_loss


prices = list(map(int, input().split()))
buy, sell, loss = minimize_loss(prices)
print(f"Buy in year {buy}, sell in year {sell}, with minimum loss of {loss}.")