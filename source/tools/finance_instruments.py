import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
# plt.style.use("seaborn")


class FinancialInstrument():
    def __init__(self, ticker, start, end):
        self.ticker = ticker
        self.start  = start
        self.end    = end
        self.get_data()
        # self.log_returns()

    def get_data(self):
        raw = yf.download(self.ticker, self.start, self.end)#.Close().to_frame()
        raw.rename(columns={"Close": "price"}, inplace=True)
        self.data = raw

    def log_returns(self):
        self.data["log_returns"] = np.log(self.data.price/self.data.price.shift(1))
