# for
#目標：練習如何讀取清單並做簡單的運算。 題目：你有一個產品價格清單，請幫我印出每個產品
#「加上 5% 營業稅」後的價格。
prices = [100, 200, 300, 400, 500]
print("Prices with 5% sales tax:")
for price in prices:
    price_with_tax = price * 1.05
    print(f"  Original: ${price}, With tax: ${price_with_tax:.2f}")
#假如是5%折扣呢？請幫我印出每個產品「打 95 折」後的價格。
price=[500, 1000, 1500, 2000, 2500]
print("prices with 5% discount:")
for price in prices:
    price_with_discount=price*0.95
    print(f" original:${price}, with discount:${price_with_discount:,.2f}")
                                        
#while
#目標：練習「不到目標不罷休」的邏輯。 題目：小明現在有 $500 元，他每天打工賺 $120 元。請用 
#while 算出他要幾天才能存到 $1000 元？
balance=500
daily_earning=120
target=1000
days=0
while balance<target:
    balance+=daily_earning
    days+=1
    print(f"day{days}:balance=${balance:,}")
#break
#目標：練習如何「跳過」或「停止」。 題目：檢查一組交易代碼。如果是 "SKIP" 就跳過；如果是 
#"STOP" 就立刻終止。
codes = ["OK", "OK", "SKIP", "OK", "STOP", "OK"]
print("Processing transactions:") 
for c in codes:
    if c =="SKIP":
        print(f"Skipping transaction:{c}.")
        continue
    print(f"{c}")

#continue