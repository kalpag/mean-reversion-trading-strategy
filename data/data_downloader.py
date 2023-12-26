# data/data_downloader.py

import yfinance as yf
import pandas as pd
import unittest
from datetime import datetime

class DataDownloader:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    def download_data(self):
        # Download historical price data using Yahoo Finance
        data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
        return data

    def update_data(self):
        # Implement logic to update historical data if needed
        # For demonstration purposes, we'll simply call download_data in this example
        updated_data = self.download_data()

        # Merge updated data with existing data (if any)
        # Assuming that 'Date' is the index in your DataFrame
        # Replace 'Date' with the actual column name if different
        existing_data = pd.read_csv('historical_data.csv', index_col='Date', parse_dates=True, infer_datetime_format=True)
        combined_data = pd.concat([existing_data, updated_data])

        # Save the combined data back to the file
        combined_data.to_csv('historical_data.csv')

class TestDataDownloader(unittest.TestCase):
    def setUp(self):
        # Set up a DataDownloader instance for testing
        self.downloader = DataDownloader(ticker='AAPL', start_date='2022-01-01', end_date='2022-12-31')

    def tearDown(self):
        # Clean up any resources used during testing
        pass

    def test_download_data(self):
        # Ensure download_data returns a DataFrame
        data = self.downloader.download_data()
        self.assertIsInstance(data, pd.DataFrame)

    def test_update_data(self):
        # Ensure update_data updates the existing data file
        # For simplicity, let's assume there's an existing data file to update
        # You might need to create a test data file for more realistic testing
        initial_data = pd.DataFrame({'Close': [100, 110, 95]}, index=pd.to_datetime(['2022-01-01', '2022-01-02', '2022-01-03']))
        initial_data.to_csv('historical_data.csv')

        # Call update_data
        self.downloader.update_data()

        # Check if the data file is updated
        updated_data = pd.read_csv('historical_data.csv', index_col='Date', parse_dates=True, infer_datetime_format=True)
        self.assertGreater(len(updated_data), len(initial_data))

if __name__ == '__main__':
    unittest.main()
