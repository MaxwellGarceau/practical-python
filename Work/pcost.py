# pcost.py
#
# Exercise 1.27

total = None
file = open('Data/portfolio.csv', 'rt')
next(file) # skip headers
for line in file:
    row = line.split(',')

    # 3 rows
    if len(row) < 3:
        continue

    # Share and price validation
    try:
        shares = int(row[1])
        price = float(row[2])
    except (ValueError, IndexError):
        # Skip lines with invalid or missing data
        continue

    # Initialize total on first valid row
    # Prevents type errors
    if total is None:
        total = 0.0

    total += int(shares) * float(price)

file.close()

if total is None:
    print('No valid shares or prices found in the file.')
else:
    print('Total cost ' + str(total))
