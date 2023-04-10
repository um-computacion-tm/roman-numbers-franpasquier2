import unittest
from Decimal_a_romano import decimal_a_romano
from Romano_a_Decimal import roman_to_decimal
class TestRomanToDecimal(unittest.TestCase):

    def test_I(self):

        resultado = roman_to_decimal('I')

        self.assertEqual(resultado, 1)

    def test_II(self):

        resultado = roman_to_decimal('II')

        self.assertEqual(resultado, 2)

    def test_III(self):

        resultado = roman_to_decimal('III')

        self.assertEqual(resultado, 3)

    def test_V(self):

        resultado = roman_to_decimal('V')

        self.assertEqual(resultado, 5)

    def test_X(self):

        resultado = roman_to_decimal('X')

        self.assertEqual(resultado, 10)

    def test_VI(self):

        resultado = roman_to_decimal('VI')

        self.assertEqual(resultado, 6)

    def test_VII(self):

        resultado = roman_to_decimal('VII')

        self.assertEqual(resultado, 7)

    def test_IV(self):

        resultado = roman_to_decimal('IV')

        self.assertEqual(resultado, 4)

    def test_IX(self):

        resultado = roman_to_decimal('IX')

        self.assertEqual(resultado, 9)

class TestDecimalRoman(unittest.TestCase):
    
    def test_1(self):

        resultado = decimal_a_romano(1)

        self.assertEqual(resultado, "I")

    def test_2(self):

        resultado = decimal_a_romano(2)

        self.assertEqual(resultado, "II")

    def test_3(self):

        resultado = decimal_a_romano(3)

        self.assertEqual(resultado, "III")

    def test_4(self):

        resultado = decimal_a_romano(4)

        self.assertEqual(resultado, "IV")
    
    def test_5(self):

        resultado = decimal_a_romano(5)

        self.assertEqual(resultado, "V")
    
    def test_10(self):

        resultado = decimal_a_romano(10)

        self.assertEqual(resultado, "X")

    def test_11(self):

        resultado = decimal_a_romano(11)

        self.assertEqual(resultado, "XI")

    def test_12(self):

        resultado = decimal_a_romano(12)

        self.assertEqual(resultado, "XII")

    def test_13(self):

        resultado = decimal_a_romano(13)

        self.assertEqual(resultado, "XIII")
    
    def test_14(self):

        resultado = decimal_a_romano(14)

        self.assertEqual(resultado, "XIV")

    def test_15(self):

        resultado = decimal_a_romano(15)

        self.assertEqual(resultado, "XV")

    def test_16(self):

        resultado = decimal_a_romano(16)

        self.assertEqual(resultado, "XVI")

    def test_17(self):

        resultado = decimal_a_romano(17)

        self.assertEqual(resultado, "XVII")

    def test_18(self):

        resultado = decimal_a_romano(18)

        self.assertEqual(resultado, "XVIII")
    
    def test_19(self):

        resultado = decimal_a_romano(19)

        self.assertEqual(resultado, "IX")
    
    def test_20(self):

        resultado = decimal_a_romano(20)

        self.assertEqual(resultado, "XX")

if __name__ == '__main__':

    unittest.main()

    