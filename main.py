import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
from pmdarima import auto_arima
from sklearn.metrics import mean_absolute_error

# Step 1: Load and preprocess the data
file_path = 'GrippeWeb_Daten_des_Wochenberichts.tsv'  # Replace with your file path
data = pd.read_csv(file_path, sep='\t')

# Filter data for "Bundesweit" and aggregate Inzidenz
data_bundesweit = data[data['Region'] == 'Bundesweit']
data_bundesweit['Kalenderwoche'] = pd.to_datetime(data_bundesweit['Kalenderwoche'] + '-1', format='%Y-W%W-%w')
time_series = data_bundesweit.groupby('Kalenderwoche')['Inzidenz'].sum().reset_index()
time_series = time_series.sort_values('Kalenderwoche')

# Step 2: Visualize the time series
plt.figure(figsize=(12, 6))
plt.plot(time_series['Kalenderwoche'], time_series['Inzidenz'], marker='o', label='Inzidenz')
plt.title('Weekly Incidences (Bundesweit Region)', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Inzidenz', fontsize=14)
plt.grid(True)
plt.legend(fontsize=12)
plt.show()

# Step 3: Stationarity Check with ADF Test
def check_stationarity(ts):
    result = adfuller(ts)
    print("ADF Statistic:", result[0])
    print("p-value:", result[1])
    print("Critical Values:", result[4])
    print("Stationary:", result[1] < 0.05)

check_stationarity(time_series['Inzidenz'])

# Step 4: Differencing if necessary
time_series['Inzidenz_diff'] = time_series['Inzidenz'].diff()
time_series.dropna(inplace=True)

# Recheck stationarity after differencing
check_stationarity(time_series['Inzidenz_diff'])

# Step 5: Train-Test Split
train_size = int(len(time_series) * 0.8)
train, test = time_series[:train_size], time_series[train_size:]

# Step 6: Auto-ARIMA for model selection
model = auto_arima(
    train['Inzidenz'],
    seasonal=True,
    m=52,  # Weekly seasonality
    trace=True,
    error_action='ignore',
    suppress_warnings=True
)

print(model.summary())

# Step 7: Fit the ARIMA model
arima_model = ARIMA(train['Inzidenz'], order=model.order, seasonal_order=model.seasonal_order).fit()

# Step 8: Forecasting
forecast_steps = len(test)
forecast = arima_model.forecast(steps=forecast_steps)
test['Forecast'] = forecast

# Step 9: Evaluate the model
mae = mean_absolute_error(test['Inzidenz'], test['Forecast'])
print("Mean Absolute Error:", mae)

# Step 10: Plot actual vs forecast
plt.figure(figsize=(12, 6))
plt.plot(train['Kalenderwoche'], train['Inzidenz'], label='Train')
plt.plot(test['Kalenderwoche'], test['Inzidenz'], label='Actual')
plt.plot(test['Kalenderwoche'], test['Forecast'], label='Forecast')
plt.title('Actual vs Forecast', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Inzidenz', fontsize=14)
plt.legend(fontsize=12)
plt.show()

# Step 11: Forecast next 5 weeks
future_forecast = arima_model.forecast(steps=5)
future_dates = pd.date_range(start=test['Kalenderwoche'].iloc[-1] + pd.Timedelta(weeks=1), periods=5, freq='W-MON')
forecast_df = pd.DataFrame({'Date': future_dates, 'Forecast': future_forecast})

print("Next 5 Weeks Forecast:")
print(forecast_df)
