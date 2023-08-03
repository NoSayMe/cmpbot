import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
# plt.style.use("seaborn")


class FinancialInstrumentBase():
    def __init__(self, ticker, start, end):
        self.data = None

        self._ticker = ticker
        self.start  = start
        self.end    = end

        self.get_data()
        self.log_returns()

    def __repr__(self):
        return f"FinancialInstrument(ticker={self._ticker}, start={self.start}, end={self.end})"

    def get_data(self):
        raw = yf.download(self._ticker, self.start, self.end).Close.to_frame()
        raw.rename(columns={"Close": "price"}, inplace=True)
        self.data = raw

    def log_returns(self):
        self.data["log_returns"] = np.log(self.data.price/self.data.price.shift(1))

    def plot_prices(self):
        self.data.price.plot(figsize=(12, 8))
        plt.title(f"Price Chart: {self._ticker}", fontsize=15)
        plt.show()

    def plot_returns(self, kind="ts"):
        if kind == "ts":
            self.data.log_returns.plot(figsize=(12, 8))
            plt.title(f"Returns: {self._ticker}", fontsize=15)
        elif kind == "hist":
            self.data.log_returns.hist(figsize=(12, 8), bins=int(np.sqrt(len(self.data))))
            plt.title(f"Frequency of returns: {self._ticker}", fontsize=15)
        plt.show()

    def set_ticker(self, ticker=None):
        if ticker is not None:
            self._ticker = ticker
            self.get_data()
            self.log_returns()


class RiskReturn(FinancialInstrumentBase):
    def __init__(self, ticker, start, end, freq=None):
        self.freq = freq
        super().__init__(ticker, start, end)

    def __repr__(self):
        return f"RiskReturn(ticker={self._ticker}, start={self.start}, end={self.end})"

    def mean_returns(self, freq=None):
        if self.freq is None:
            return self.data.log_returns.mean()
        else:
            resampled_price = self.data.price.resample(self.freq).last()
            resampled_returns = np.log(resampled_price/resampled_price.shift(1))
            return resampled_returns.mean()

    def std_returns(self):
        if self.freq is None:
            return self.data.log_returns.std()
        else:
            resampled_price = self.data.price.resample(self.freq).last()
            resampled_returns = np.log(resampled_price / resampled_price.shift(1))
            return resampled_returns.std()

    def annualized_perf(self):
        mean_return = round(self.data.log_returns.mean() * 252, 3)
        risk = round(self.data.log_returns.std() * np.sqrt(252), 3)
        print(f"Return: {mean_return} | Risk: {risk}")
