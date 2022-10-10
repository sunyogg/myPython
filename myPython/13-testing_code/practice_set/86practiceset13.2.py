import unittest
from employeeclassmodule import Employee

class TestEmployeeClass(unittest.TestCase):


    def setUp(self):
        self.em1 = Employee('david','john',70000)
        self.raisepay = [7000,10000]


    def test_give_default_raise(self):
        """Test to check the default raise is working fine."""
        self.em1.raise_pay()


    def test_give_custom_raise(self):
        """Test to check the custom raise is working fine."""
        self.em1.raise_pay(self.raisepay[0])


if __name__ == '__main__':
    unittest.main()


