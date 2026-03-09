# break — exit the loop early
sales_figures = [8_200, 11_500, 6_800, -500, 14_200, 9_900]

print("Validating sales records:")
for i, sale in enumerate(sales_figures):
    if sale < 0:
        print(f"  ERROR: Negative sale at record {i} — stopping validation.")
        break
    print(f"  Record {i}: ${sale:,} — OK")