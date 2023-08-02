

class FinancialInstrument():
    def __init__(self, ticker, start, end):
        self.ticker = ticker
        self.start  = start
        self.end    = end

    def say_hi(self):
        print(f"Hi from {self.ticker}")
