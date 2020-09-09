import unittest
from Block import *
from Transaction import *
from ecdsa import SigningKey, NIST384p

class UnitTest(unittest.TestCase):
        def hash(self):
            self.assertEqual(calculateHash(0, "", 1465154705, [], 0, 0), "")