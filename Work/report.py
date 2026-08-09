#! /usr/bin/env python3
# report.py
#
# Exercise 2.4


import csv
from Models.portfolio_item import PortfolioItem
from pathlib import Path
from fileparse import parse_csv

BASE_DIR = Path(__file__).resolve().parent.as_posix()

def read_portfolio(filename):
    '''Opens a given portfolio file and reads it into a list of tuples'''

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        portfolio = parse_csv(rows, headers, [str, int, float])
    return portfolio

def read_prices(filename):
    'reads a set of prices such as this into a dictionary where the keys of the dictionary are the stock names and the values in the dictionary are the stock prices'
    f = open(filename, 'r')
    rows = csv.reader(f)
    price_dict = {}
    for row in rows:
        if row:
            price_dict[str(row[0])] = float(row[1])
    return price_dict

def make_report(portfolio: list[PortfolioItem], prices: dict[str, float]):
    'Takes a list of portfolio stocks and dictionary of prices as input and returns a list of portfolio tuples'

    # Create an entirely independent copy of the data structure
    report = []

    for holding in portfolio:

        # Calculate stock price change

        # Assuming that all stocks are in current_prices
        # Otherwise, we would have to add defensive guards here
        current_price = prices[holding['name']]
        price_change = current_price - holding['price']

        report.append((holding['name'], holding['shares'], holding['price'], price_change))

    return report

def print_table(report):

    headers = ('Name', 'Shares', 'Price', 'Change')
    h_list: list[str] = []
    for h in headers:
        h_list.append(f'{h:>10s}')

    print(" ".join(h_list))

    separator_list = [f'{"":->10s}'] * 4
    print(" ".join(separator_list))

    for name, shares, price, change in report:
        price = f'${price:.2f}'
        print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')

def portfolio_report(portfolio_filename=(BASE_DIR + '/Data/portfolio.csv'), prices_filename=(BASE_DIR + '/Data/prices.csv')):
    '''
    Orchestration layer
    '''
    # List of stock holdings
    # Ex: {'name': 'AA', 'price': 32.2, 'shares': 100}
    portfolio = read_portfolio(portfolio_filename)

    # Stock name -> current price
    # Ex: {'AA': 20.0}
    current_prices = read_prices(prices_filename)
    report = make_report(portfolio, current_prices)
    print_table(report)

def main(argv):
    portfolio = argv[1]
    prices = argv[2]

    portfolio_report(portfolio, prices)

# >>> import report
# >>> report.main(['report.py', 'Data/portfolio.csv', 'Data/prices.csv'])
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        raise SystemExit(f'Too few arguments. Usage: {sys.argv[0]} ' 'portfile pricefile')
    main(sys.argv)
    sys.exit(0)
