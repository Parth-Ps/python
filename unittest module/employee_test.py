import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpclass(cls):
        print('SetupClass')

    @classmethod
    def teardownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Corey', "Schafer", 50000)
        self.emp_2 = Employee("Sue", "Smith", 60000)

    def tearDown(self):
        print('tearDownClass\n')

    def test_email(self):
        print("test email")
        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@gmail.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@gmail.com')

    def test_fullname(self):
        print("test fullname")
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('test apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()
