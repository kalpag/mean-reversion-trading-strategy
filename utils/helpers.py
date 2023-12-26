# utils/helpers.py

def calculate_sharpe_ratio(returns):
    # Implement logic to calculate the Sharpe ratio
    # For simplicity, let's assume a risk-free rate of 0%
    average_return = returns.mean()
    risk_free_rate = 0
    standard_deviation = returns.std()

    sharpe_ratio = (average_return - risk_free_rate) / standard_deviation

    return sharpe_ratio
