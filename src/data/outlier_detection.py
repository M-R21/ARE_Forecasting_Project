import numpy as np
import pandas as pd
from scipy import stats

def detect_outliers(data):
    z_scores = np.abs(stats.zscore(data['cases']))  # Replace 'cases' with actual case column
    return data[(z_scores < 3)]
