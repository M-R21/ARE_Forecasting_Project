import pandas as pd
from src.data.outlier_detection import detect_outliers

def preprocess_data(data):
    # Data cleaning
    data.dropna(inplace=True)
    data = data.drop_duplicates()
    
    # Outlier detection
    data = detect_outliers(data)
    
    # Additional preprocessing steps
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)
    
    return data
