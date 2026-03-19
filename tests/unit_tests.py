import unittest
from dab.account import *

class DABUnitTests(unittest.TestCase):
  def test_checkWithdrawal(self):
    # cas de test n°1:
    self.assertEqual(checkWithdrawal(20,350), True)
    # cas de test n°2 :
    self.assertEqual(checkWithdrawal(490, 350), False)


if __name__ == '__main__':
  unittest.main()
