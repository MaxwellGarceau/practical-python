class Stock:
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self) -> None:
        print(self.shares * self.price)

    def sell(self, amount: int) -> None:
        self.shares = self.shares - amount

    def __repr__(self):
        values = tuple(vars(self).values())
        values = [ "'" + item + "'" if isinstance(item, str) else str(item) for item in values ]
        return 'Stock(' + ', '.join(values) + ')'