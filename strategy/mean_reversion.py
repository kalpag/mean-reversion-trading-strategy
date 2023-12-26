# strategy/mean_reversion.py

import pandas as pd
import numpy as np

class MeanReversionStrategy:
    def __init__(self, data):
        self.data = data

    def generate_signals(self, lookback_period=20, z_score_threshold=1.0):
        # Calculate rolling mean and standard deviation
        rolling_mean = self.data['Close'].rolling(window=lookback_period).mean()
        rolling_std = self.data['Close'].rolling(window=lookback_period).std()

        # Calculate Z-score
        z_score = (self.data['Close'] - rolling_mean) / rolling_std

        # Generate signals
        signals = pd.Series(index=self.data.index)
        signals[z_score > z_score_threshold] = -1  # Sell signal
        signals[z_score < -z_score_threshold] = 1  # Buy signal

        return signals

# Example usage:
# mean_reversion_strategy = MeanReversionStrategy(data)
# signals = mean_reversion_strategy.generate_signals()
