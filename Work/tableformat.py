# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''
    def headings(self, headers):
        html_list: list[str] = []
        html_list.append('<tr>')
        for h in headers:
            html_list.append('<th>' + h + '</th>')
        html_list.append('</tr>')
        print(''.join(html_list))

    def row(self, rowdata: list[tuple]):
        html_list: list[str] = []
        html_list.append('<tr>')
        for col in rowdata:
            html_list.append('<td>' + col + '</td>')
        html_list.append('</tr>')
        print(''.join(html_list))

# name: txt', 'csv', or 'html'
def create_formatter(name: str) -> TableFormatter:
    match name:
        case 'txt':
            return TextTableFormatter()
        case 'csv':
            return CSVTableFormatter()
        case 'html':
            return HTMLTableFormatter()
        case _:
            raise ValueError('Name must be "txt", "csv", or "html"')
