#### TRY IT YOURSELF - Chapter 11 - Page 221 - Employee
import unittest
from employee_class_11_3 import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the module employee_class_11_3"""

    def setUp(self):
        """Make an employee to use in tests."""
        self.employee1 = Employee('John', 'Kelly', 25_000)
        self.employee_raise = 10000

    def test_give_default_raise(self):
        """Test that a default raise works correctly."""
        self.employee1.give_raise()
        self.assertEqual(30000, self.employee1.annual_salary)

    def test_give_custom_salary(self):
        """"""
        self.employee1.give_raise(self.employee_raise)
        self.assertEqual(35000, self.employee1.annual_salary)

if __name__ == '__main__':
    unittest.main()