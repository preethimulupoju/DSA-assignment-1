import pandas as pd

df = pd.DataFrame({'ship_mode': ['Same Day', 'First Class', 'Standard Class', 'Standard Class'],
                   'sales': [1000, 2000, 3000, 4000],
                   'profit': [100, 200, 300, 400]})

def calculate_surcharge(ship_mode):
    if ship_mode == "Same Day":
        return 0.2
    elif ship_mode == "First Class":
        return 0.1
    elif ship_mode == "Standard Class":
        return 0.05
    else:
        return 0

df['surcharge'] = df['ship_mode'].apply(calculate_surcharge)
df['total_cost'] = (df['sales'] - df['profit']) * (1 + df['surcharge'])

print(df)
