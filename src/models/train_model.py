import pandas as pd

def create_lag_features(data):
    for lag in range(1, 3):  # Create lag features for 1 and 2 weeks
        data[f'lag_{lag}'] = data['cases'].shift(lag)
    return data
