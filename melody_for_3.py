#
# Melody, 2026/3/4
# Melody_for_3.py
#Use for loop to conculate sum and len to know the number of element
#

# Accumulate a running total
sales_data = [12_000, 18_500, 9_300, 22_100, 15_600]
total = 0

for sale in sales_data:
    total += sale              # shorthand for total = total + sale

print(f"Total Sales: ${total:,}")
print(f"Average Sale: ${total / len(sales_data):,.2f}")