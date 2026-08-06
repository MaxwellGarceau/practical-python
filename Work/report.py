# report.py
#
# Exercise 2.4

import copy
import csv
from Models.portfolio_item import PortfolioItem

def read_portfolio(filename):
    '''Opens a given portfolio file and reads it into a list of tuples'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            name = str(row[0])
            nshares = int(row[1])
            price = float(row[2])
            # holding = (name, nshares, price)
            holding = {'name': name, 'shares': nshares, 'price': price}
            portfolio.append(holding)
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

def print_table():
    # List of stock holdings
    # Ex: {'name': 'AA', 'price': 32.2, 'shares': 100}
    portfolio = read_portfolio('Data/portfolio.csv')

    # Stock name -> current price
    # Ex: {'AA': 20.0}
    current_prices = read_prices('Data/prices.csv')

    report = make_report(portfolio, current_prices)

    headers = ('Name', 'Shares', 'Price', 'Change')
    h_list: list[str] = []
    for h in headers:
        h_list.append(f'{h:>10s}')

    print(" ".join(h_list))

    separator_list = [f'{"":->10s}'] * 4
    print(" ".join(separator_list))

    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
