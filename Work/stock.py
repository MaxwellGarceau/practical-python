class Stock:
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    __slots__ = ('name', '_shares', 'price')

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Must be of type int')
        self._shares = value

    @property
    def cost(self) -> None:
        print(self.shares * self.price)

    def sell(self, amount: int) -> None:
        self.shares = self.shares - amount

    def __repr__(self):
        values = [repr(value) for value in vars(self).values() ]
        return 'Stock(' + ', '.join(values) + ')'