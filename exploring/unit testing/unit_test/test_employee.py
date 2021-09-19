import unittest
from employee import Employee # import the class Employee from the module employee
# from unittest.mock import patch
import mock # if inside the tested function, there are calls to other functions that are imported

class TestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setup class")
    
    @classmethod
    def tearDownClass(cls):
        print("teardown class")

    def setUp(self):
        # runs at every start of a test function by default
        print("setup")
        self.emp1 = Employee("adam", "smith", 2500)
        self.emp2 = Employee("mary", "jane", 4500)

    def tearDown(self):
        # runs at every end of a test function by default
        print("teardown")
        pass

    def test_email(self):
        print("testing email")
        self.assertEqual(self.emp1.email, "adam.smith@gmail.com")
        self.assertEqual(self.emp2.email, "mary.jane@gmail.com")

        self.emp1.first = "john"
        self.emp2.first = "rose"

        self.assertEqual(self.emp1.email, "john.smith@gmail.com")
        self.assertEqual(self.emp2.email, "rose.jane@gmail.com")
    
    def test_fullname(self):
        print("testing fullname")
        self.emp1.last = "john"
        self.emp2.last = "rose"

        self.assertEqual(self.emp1.fullName, "adam john")
        self.assertEqual(self.emp2.fullName, "mary rose")

    def test_test(self):
        self.assertEqual(self.emp1.test(10,5),15)

if __name__ == "__main__":
    unittest.main()