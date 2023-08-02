from source.tools.finance_instruments import FinancialInstrument


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    stock = FinancialInstrument("AAPL", "2015-01-01", "2019-12-31")

    # print(stock.data.columns.values.tolist())
    # print(type(stock.data))
    stock.data.drop(columns=["Open", "High", "Low", "Adj Close", "Volume"], axis=1)
    # stock.data.drop(axis=[1, 2, 3, 5])
    # stock.data

    print(stock.data)
