# report.py
#
# Exercise 2.4

import csv

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
    price_dict = []
    for row in rows:
        if row:
            stock = {str(row[0]): float(row[1])}
            price_dict.append(stock)
    return price_dict
