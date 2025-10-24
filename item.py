from dataclasses import dataclass

@dataclass(eq=True)
class Item:
    name: str
    price: float
    count: int
