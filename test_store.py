from model import Model
from view import view
from controller import controller


def testModel():
  test_data = [{"name": "Mechanical Keyboard", "price": 120.50, "count": 5}]
  m = Model()
  result = m.read(test_data)
  assert isInstance(test_data, result)

