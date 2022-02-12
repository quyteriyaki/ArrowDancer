import unittest
from dancer import *

class TestDanceInput(unittest.TestCase):
  def test_SingleArrow(self):
    try:
      arrow = Arrow(ArrowDirection.TOP_CENTER, ArrowType.BONK)
    except Exception as e:
      self.fail(e.args)
    else:
      self.assertTrue(True)

  def test_ArrowBonk(self):
    try:
      arrow = Arrow(ArrowDirection.BOTTOM_LEFT, ArrowType.BONK)
    except Exception as e:
      self.assertEqual("Found a corner bonk in Dance Formation.", e.args[0])
    else:
      self.fail("Did not find a bonk")

  def test_ArrowShorthand(self):
    try:
      arrow = Arrow.short("1P")
    except Exception as e:
      self.fail(e.args)
    else:
      self.assertTrue(True)

  def test_danceFormationSingle(self):
    try:
      forma = DanceFormation(Arrow.short("1P"))
    except Exception as e:
      self.fail(e.args)
    else:
      self.assertTrue(True)
  
  def test_danceFormationMultiple(self):
    try:
      forma = DanceFormation.multiShort("1P, 2B")
    except Exception as e:
      self.fail(e.args)
    else:
      self.assertTrue(True)
  
  def test_danceMultipleList(self):
    try:
      forma = DanceFormation.multiShort(("1P", "2B"))
      forma = DanceFormation.multiShort(["1P", "2B"])
    except Exception as e:
      self.fail(e.args)
    else:
      self.assertTrue(True)

if __name__ == "__main__":
  unittest.main()