def piotroski_fscore(curr, prev):
    score = 0
    signals = {}

    # --- Profitability ---
    roa_curr = curr['net_income'] / curr['total_assets']
    roa_prev = prev['net_income'] / prev['total_assets']

    signals['ROA > 0'] = 1 if roa_curr > 0 else 0
    signals['CFO > 0'] = 1 if curr['cfo'] > 0 else 0
    signals['ROA improved'] = 1 if roa_curr > roa_prev else 0
    signals['CFO > Net Income'] = 1 if curr['cfo'] > curr['net_income'] else 0

    # --- Leverage & Liquidity ---
    debt_ratio_curr = curr['long_term_debt'] / curr['total_assets']
    debt_ratio_prev = prev['long_term_debt'] / prev['total_assets']
    signals['Debt ratio down'] = 1 if debt_ratio_curr < debt_ratio_prev else 0

    current_ratio_curr = curr['current_assets'] / curr['current_liabilities']
    current_ratio_prev = prev['current_assets'] / prev['current_liabilities']
    signals['Current ratio up'] = 1 if current_ratio_curr > current_ratio_prev else 0

    signals['No dilution'] = 1 if curr['shares_outstanding'] <= prev['shares_outstanding'] else 0

    # --- Efficiency ---
    gm_curr = (curr['revenue'] - curr['cogs']) / curr['revenue']
    gm_prev = (prev['revenue'] - prev['cogs']) / prev['revenue']
    signals['Gross margin up'] = 1 if gm_curr > gm_prev else 0

    at_curr = curr['revenue'] / curr['total_assets']
    at_prev = prev['revenue'] / prev['total_assets']
    signals['Asset turnover up'] = 1 if at_curr > at_prev else 0

    score = sum(signals.values())

    return score, signals


current_year = {
    'net_income': 5000, 'total_assets': 40000, 'cfo': 6000,
    'revenue': 30000, 'cogs': 18000, 'current_assets': 12000,
    'current_liabilities': 6000, 'long_term_debt': 8000,
    'shares_outstanding': 1000
}

previous_year = {
    'net_income': 4000, 'total_assets': 38000, 'cfo': 3000,
    'revenue': 27000, 'cogs': 17000, 'current_assets': 10000,
    'current_liabilities': 6500, 'long_term_debt': 9000,
    'shares_outstanding': 1000
}

score, signals = piotroski_fscore(current_year, previous_year)
print(f"F-Score: {score}/9")
for k, v in signals.items():
    print(f"  {k}: {v}")