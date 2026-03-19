import unittest
from dab.account import *

class DABUnitTests(unittest.TestCase):
  def test_checkWithdrawal(self):
    # cas de test n°1:
    self.assertEqual(checkWithdrawal(20,350), True)


if __name__ == '__main__':
  unittest.main()
