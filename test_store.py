from model import Model
from view import view
from controller import controller
from item import Item

def testModel():
  test_data = [{"name": "Mechanical Keyboard", "price": 120.50, "count": 5}]
  m = Model()
  result = m.read(test_data)
  ideal = [Item(name='Mechanical Keyboard', price=120.5, count=5)]
  assert isInstance(result, ideal)

