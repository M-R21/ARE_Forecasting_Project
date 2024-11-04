import matplotlib.pyplot as plt

def plot_predictions(actual, predicted):
    plt.figure(figsize=(10, 5))
    plt.plot(actual.index, actual, label='Actual Cases')
    plt.plot(actual.index, predicted, label='Predicted Cases')
    plt.legend()
    plt.show()
