from dataclasses import dataclass

@dataclass
class PortfolioItem:
    name: str
    price: float
    shares: int
