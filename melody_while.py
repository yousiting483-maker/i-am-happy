balance=30000
rate=0.07
traget=150000
year=0
while balance<traget:
    balance=balance*(1+rate)
    year+=1
print(f"Investment doubles in {year} years")
print(f"Final balance: {balance:.2f}")
