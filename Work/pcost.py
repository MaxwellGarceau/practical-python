# pcost.py
#
# Exercise 1.27
import csv, sys

def portfolio_cost(filename):
    'This function takes a filename as input, reads the portfolio data in that file, and returns the total cost of the portfolio as a float.'
    total = None
    file = open(filename, 'rt')
    rows = csv.reader(file)
    next(rows) # skip headers
    for row in rows:

        # 3 rows
        if len(row) < 3:
            continue

        # Share and price validation
        try:
            name, shares, price = portfolio_tuple(row)
        except ValueError as error:
            print('Invalid shares or prices')
            print(f"Error: {error}")
            continue
        except IndexError as error:
            print(f"IndexError: {error}")
            continue

        # Initialize total on first valid row
        # Prevents type errors
        if total is None:
            total = 0.0

        total += int(shares) * float(price)

    file.close()

    if total is None:
        raise RuntimeError('No valid shares or prices found in the file.')

    return total

# Model
def portfolio_tuple(row):
    'name, shares, price'
    return (row[0], int(row[1]), float(row[2]))

# Orchestration

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)