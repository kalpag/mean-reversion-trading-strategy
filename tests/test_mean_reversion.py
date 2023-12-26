# tests/test_mean_reversion.py

import unittest
import pandas as pd
from datetime import datetime
from strategy.mean_reversion import MeanReversionStrategy

class TestMeanReversionStrategy(unittest.TestCase):
    def setUp(self):
        # Set up a MeanReversionStrategy instance for testing
        data = pd.DataFrame({'Close': [100, 110, 95, 105, 120]},
                            index=pd.to_datetime(['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05']))
        self.strategy = MeanReversionStrategy(data)

    def tearDown(self):
        # Clean up any resources used during testing
        pass

    def test_generate_signals(self):
        # Ensure generate_signals returns a Series with buy/sell signals
        signals = self.strategy.generate_signals(lookback_period=3, z_score_threshold=0.5)
        self.assertIsInstance(signals, pd.Series)
        self.assertTrue(all(signal in [-1, 0, 1] for signal in signals))

if __name__ == '__main__':
    unittest.main()
