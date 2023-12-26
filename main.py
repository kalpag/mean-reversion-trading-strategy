# main.py

from data.data_downloader import DataDownloader
from data.preprocessing import DataPreprocessor
from strategy.mean_reversion import MeanReversionStrategy
from backtesting.backtester import Backtester
from utils.helpers import calculate_sharpe_ratio

def main():
    # Set parameters
    ticker = 'AAPL'
    start_date = '2022-01-01'
    end_date = '2022-12-31'
    lookback_period = 20
    z_score_threshold = 1.0

    # Step 1: Download and preprocess data
    data_downloader = DataDownloader(ticker, start_date, end_date)
    raw_data = data_downloader.download_data()

    data_preprocessor = DataPreprocessor(raw_data)
    cleaned_data = data_preprocessor.clean_data()
    preprocessed_data = data_preprocessor.preprocess_data()

    # Step 2: Define and apply trading strategy
    mean_reversion_strategy = MeanReversionStrategy(preprocessed_data)
    signals = mean_reversion_strategy.generate_signals(lookback_period, z_score_threshold)

    # Step 3: Backtest the strategy
    backtester = Backtester(preprocessed_data, signals)
    final_balance = backtester.conduct_backtest()

    # Step 4: Evaluate performance
    returns = preprocessed_data['Close'].pct_change().dropna()
    sharpe_ratio = calculate_sharpe_ratio(returns)

    # Step 5: Display results
    print(f"Initial Balance: $100,000")
    print(f"Final Balance: ${final_balance:.2f}")
    print(f"Sharpe Ratio: {sharpe_ratio:.4f}")

#if __name__ == "__main__":
  #  main()
