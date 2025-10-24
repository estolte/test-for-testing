from model.py import model
from view.py import view
from controller.py import controller

# 1. Basic palindrome
assert model({ "name": "Mechanical Keyboard", "price": 120.50, "count": 5 }) == [Item(name='Mechanical Keyboard', price=120.5, count=5)]

