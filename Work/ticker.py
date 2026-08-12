# ticker.py

from follow import follow
import csv
import report
import tableformat

def ticker(portfile, logfile, fmt='txt'):
    portfolio = report.read_portfolio(portfile)
    formatter = tableformat.create_formatter(fmt)

    lines = follow(logfile)
    rows = parse_stock_data(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    rows = filter_symbols(rows, portfolio)
    # for row in rows:
    #     print(row)

    formatter.headings(['Name','Price','Change'])
    for r in rows:
        rowdata = [ r["name"], f'{r["price"]:0.2f}', f'{r["change"]:0.2f}' ]
        formatter.row(rowdata)

def parse_stock_data(lines):
    rows = csv.reader(lines)
    return rows

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def main(args):
    if len(args) < 3:
        raise SystemExit('Usage: %s portfile logfile output_format' % args[0])
    format = args[3] if 3 < len(args) else 'txt'
    ticker(portfile=args[1], logfile=args[2], fmt=format)

if __name__ == '__main__':
    import sys
    main(sys.argv)

    # portfolio = report.read_portfolio('Data/portfolio.csv')

    # lines = follow('Data/stocklog.csv')
    # rows = parse_stock_data(lines)
    # rows = select_columns(rows, [0, 1, 4])
    # rows = convert_types(rows, [str, float, float])
    # rows = make_dicts(rows, ['name', 'price', 'change'])
    # # rows = filter_symbols(rows, portfolio)
    # rows = filter_symbols(rows, [p.name for p in portfolio])
    # for row in rows:
    #     print(row)
