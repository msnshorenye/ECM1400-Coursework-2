import pytest
from Components import switch_colour
from game_engine import cli_coords_input
def test_switch_colour():

  assert switch_colour("Light") == "Dark"

if __name__ == "__main__":
  
  try:
    test_switch_colour()
  except AssertionError as message:
     print(message)
   
switch_colour("Light")
  