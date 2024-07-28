import yfinance as yf
import pandas as pd

def get_stock_data(tickers):
    data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period='1d')
        current_price = hist['Close'].iloc[-1]
        data[ticker] = current_price
    return data

def display_portfolio(portfolio):
    print(f"{'Ticker':<10} {'Shares':<10} {'Price':<10} {'Value':<10}")
    print('-' * 40)
    total_value = 0
    for ticker, (shares, price) in portfolio.items():
        value = shares * price
        total_value += value
        print(f"{ticker:<10} {shares:<10} {price:<10.2f} {value:<10.2f}")
    print('-' * 40)
    print(f"{'Total Value':<30} {total_value:<10.2f}")

def main():
    # Define your portfolio here: ticker, number of shares
    portfolio = {
        'AAPL': (10, 0),  # Apple Inc, 10 shares
        'GOOGL': (5, 0),  # Alphabet Inc, 5 shares
        'MSFT': (8, 0)    # Microsoft Corp, 8 shares
    }

    # Get current prices
    tickers = portfolio.keys()
    prices = get_stock_data(tickers)
    
    # Update portfolio with current prices
    for ticker in portfolio:
        shares, _ = portfolio[ticker]
        portfolio[ticker] = (shares, prices[ticker])
    
    # Display portfolio
    display_portfolio(portfolio)

if __name__ == "__main__":
    main()
