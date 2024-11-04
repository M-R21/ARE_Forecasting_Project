from sklearn.metrics import mean_absolute_error, mean_squared_error
import pickle

def evaluate_model(model_path, test_data):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    # Predictions
    predictions = model.predict(test_data)

    # Calculate metrics
    mae = mean_absolute_error(test_data['cases'], predictions)
    mse = mean_squared_error(test_data['cases'], predictions)

    print(f'MAE: {mae}, MSE: {mse}')
