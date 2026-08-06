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
    report_portfolio = copy.deepcopy(portfolio)


    for holding in report_portfolio:

        # Calculate stock price change

        # Assuming that all stocks are in current_prices
        # Otherwise, we would have to add defensive guards here
        current_price = prices[holding['name']]
        price_change = current_price - holding['price']

        holding['change'] = price_change

    return report_portfolio

# # Calculate portfolio total and change in this function
# # The code is messy, but this avoid running multiple loops for a simple task
# def get_change():
#     'Get portfolio total and change for current dates stock prices'
#     # List of stock holdings
#     # Ex: {'name': 'AA', 'price': 32.2, 'shares': 100}
#     portfolio = read_portfolio('Data/portfolio.csv')

#     # Stock name -> current price
#     # Ex: {'AA': 20.0}
#     current_prices = read_prices('Data/prices.csv')

#     portfolio_total = 0.0
#     change_total = 0.0
#     for holding in portfolio:

#         # Calculate stock price change

#         # Assuming that all stocks are in current_prices
#         # Otherwise, we would have to add defensive guards here
#         current_price = current_prices[holding['name']]
#         price_change = current_price - holding['price']

#         # Sum portfolio total
#         portfolio_total += holding['price'] * holding['shares']
#         change_total += price_change * holding['shares']

#     new_total = portfolio_total + change_total

#     print('Initial portfolio value: ', f"{portfolio_total:.2f}")
#     print('Total value change: ', f"{change_total:.2f}")
#     print('New portfolio value: ', f"{new_total:.2f}")
