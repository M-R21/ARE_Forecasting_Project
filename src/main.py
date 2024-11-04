from src.utils.config import load_config
from src.utils.logger import setup_logger
from src.data.load_data import load_data
from src.data.preprocess_data import preprocess_data
from src.models.train_model import train_arima_model, train_lstm_model

def main():
    config = load_config('config.yaml')
    setup_logger(config['logging']['log_file'])

    # Load and preprocess data
    raw_data = load_data(config['data']['raw_data_path'])
    cleaned_data = preprocess_data(raw_data)

    # Save cleaned data
    cleaned_data.to_csv(config['data']['processed_data_path'], index=False)

    # Train models
    train_arima_model(config['data']['processed_data_path'])
    train_lstm_model(config['data']['processed_data_path'])

if __name__ == "__main__":
    main()
