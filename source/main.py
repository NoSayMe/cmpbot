from tools.finance_instruments import FinancialInstrument


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    stock = FinancialInstrument("AAPL", "dnes", "vsera")
    stock.say_hi()
