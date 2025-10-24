from model import Model
from view import View
from controller import Controller
from item import Item
import json

def testModel():
  test_data = [{"name": "Mechanical Keyboard", "price": 120.50, "count": 5}]
  filepath = "temp_inventory.json"

    # write to JSON file
  with open(filepath, "w") as f:
    json.dump(test_data, f)
  
  m = Model()
  result = m.read(filepath)
  ideal = [Item(name='Mechanical Keyboard', price=120.5, count=5)]
  assert isinstance(result, list)
  assert result == ideal

