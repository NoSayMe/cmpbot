from source.tools.finance_instruments import FinancialInstrumentBase
from source.tools.finance_instruments import RiskReturn


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    stock = RiskReturn("AAPL", "2015-01-01", "2019-12-31")

    # print(stock.data.info())
    # print(stock.data)

    stock.plot_prices()
    # stock.plot_returns("hist")

    # stock.set_ticker("GE")
    # stock.plot_prices()

    print(stock.mean_returns())
    print(stock.mean_returns("m"))
    print(stock.std_returns())
    print(stock.std_returns("m"))
    print(stock.annualized_perf())
