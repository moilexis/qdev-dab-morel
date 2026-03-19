import unittest
from dab.account import *

class DABUnitTests(unittest.TestCase):
  def test_checkWithdrawal(self):
    # cas de test n°1:
    self.assertEqual(checkWithdrawal(350,20), True)
    # cas de test n°2 :
    self.assertEqual(checkWithdrawal(350, 490), False)
    # cas de test n°3 :
    self.assertEqual(checkWithdrawal(3050,500 ), False)


if __name__ == '__main__':
  unittest.main()
