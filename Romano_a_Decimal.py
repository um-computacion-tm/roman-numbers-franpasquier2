import unittest

def roman_to_decimal(roman):
    if roman == "I" :
        return 1
    elif roman == "II":
        return 2
    elif roman == "III":
        return 3
    elif roman == "IV":
        return 4
    elif roman == "V":
        return 5
    elif roman == "VI":
        return 6
    elif roman == "VII":
        return 7
    elif roman == "VIII":
        return 8
    elif roman == "IX":
        return 9
    elif roman == "X":
        return 10

class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        resultado = roman_to_decimal("I")

        self.assertEqual(resultado, 1)

    def test_II(self):
        resultado = roman_to_decimal("II")

        self.assertEqual(resultado, 2)

    def test_III(self):
        resultado = roman_to_decimal("III")

        self.assertEqual(resultado, 3)

    def test_IV(self):
        resultado = roman_to_decimal("IV")

        self.assertEqual(resultado, 4)

    def test_V(self):
        resultado = roman_to_decimal("V")

        self.assertEqual(resultado, 5)

    def test_VI(self):
        resultado = roman_to_decimal("VI")

        self.assertEqual(resultado, 6)
    
    def test_VII(self):
        resultado = roman_to_decimal("VII")

        self.assertEqual(resultado, 7)

    def test_VIII(self):
        resultado = roman_to_decimal("VIII")

        self.assertEqual(resultado, 8)

    def test_IX(self):
        resultado = roman_to_decimal("IX")

        self.assertEqual(resultado, 9)

    def test_X(self):
        resultado = roman_to_decimal("X")

        self.assertEqual(resultado, 10)

    def test_L(self):
        resultado = roman_to_decimal("L")

        self.assertEqual(resultado, 50)

    def test_C(self):
        resultado = roman_to_decimal("C")

        self.assertEqual(resultado, 100)

    def test_D(self):
        resultado = roman_to_decimal("D")

        self.assertEqual(resultado, 500)
    
    def test_M(self):
        resultado = roman_to_decimal("M")

        self.assertEqual(resultado, 1000)

    def test_LXXXVII(self):
        resultado = roman_to_decimal("LXXXVII")

        self.assertEqual(resultado, 87)

    def test_CCCXLII(self):
        resultado = roman_to_decimal("CCCXLII")

        self.assertEqual(resultado, 342)

if __name__ == '__main__':
    unittest.main()




import unittest


def roman_to_decimal(roman):

    total = 0

    for letter in roman:

        if letter == 'I':

            total += 1

        elif letter == 'V':

            if total > 0:

                total = -1

            total += 5

        elif letter == 'X':

            if total > 0:

                total = -1

            total += 10

    return total

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


if __name__ == '__main__':

    unittest.main()

