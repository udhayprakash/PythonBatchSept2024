import unittest


mytype = int | float | str

def addition(num1: mytype, num2: mytype) -> mytype:
    if isinstance(num1, str):
        num1 = float(num1)
        
    if isinstance(num2, str):
        num2 = float(num2)
    return round(num1 + num2, 2)


class TestAddition(unittest.TestCase):
    def test_all_integers_positive(self):
        self.assertEqual(addition(0, 0) , 0)
        self.assertEqual(addition(0, 1) , 1)
        self.assertEqual(addition(1, 0) , 1)
        self.assertEqual(addition(1, -1) , 0) 
        self.assertEqual(addition(1, -1), 0)
        
    def test_all_integers_mixed(self):
        self.assertEqual(addition(2, 3) , 5)
        self.assertEqual(addition(-2, 3) , 1)
        self.assertEqual(addition(-2, -3) , -5)

    def test_all_float_values(self):
        self.assertEqual(addition(0, 0.0) , 0.0)
        self.assertEqual(addition(0, 1.0) , 1.0)
        self.assertEqual(addition(1.5, 0) , 1.5)

    def test_all_float_negative_values(self):
        self.assertEqual(addition(1.2, -0.9) , 0.3)


    def test_string_and_integer_combinations(self):
        self.assertEqual(addition('12', '13') , 25)
        self.assertEqual(addition(12, '13') , 25)
        self.assertEqual(addition('12', 13) , 25)
        self.assertEqual(addition(12, 13) , 25)


    def test_string_and_float_combinations(self):
        self.assertEqual(addition('12.5', '13.0') , 25.5)
        self.assertEqual(addition(12.0, '13.0') , 25.0)
        self.assertEqual(addition('0.12', 13) ,  13.12)
        self.assertEqual(addition(1.2, -1.3) , -0.1)



# command line execution command
# python -m unittest -v 
# NOTE: ensure that the test script is either starting with test_
# or ending with _test
