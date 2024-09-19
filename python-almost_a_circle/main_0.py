import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

class TestBase(unittest.TestCase):
    def test_auto_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_custom_id(self):
        b = Base(89)
        self.assertEqual(b.id, 89)
