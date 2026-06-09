def sloan_ratio(net_income, cfo, total_assets_curr, total_assets_prev):
    avg_assets = (total_assets_curr + total_assets_prev) / 2
    accruals = net_income - cfo
    ratio = accruals / avg_assets
    return ratio, accruals


net_income = 5000
cfo = 2000          
total_assets_curr = 40000
total_assets_prev = 38000

ratio, accruals = sloan_ratio(net_income, cfo, total_assets_curr, total_assets_prev)

print(f"Accruals: {accruals}")
print(f"Sloan Ratio: {ratio:.4f}")

if ratio > 0.1:
    print("Red flag earnings quality poor")
elif ratio < 0:
    print("Healthy cash flow exceeds earnings")
else:
    print("Acceptable range")