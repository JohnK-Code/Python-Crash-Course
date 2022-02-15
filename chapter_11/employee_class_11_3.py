#### TRY IT YOURSELF - Chapter 11 - Page 221 - Employee
class Employee:
    """A class to represent an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Store employee name and salary."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.annual_salary = annual_salary

    def give_raise(self, employee_raise=5000):
        """Increase the employees salary by the raise amount."""
        self.annual_salary = self.annual_salary + employee_raise
