
"""""
import unittest


def decimal_to_roman(decimal):

    total = ''

    if decimal >= 100:

        centena = decimal // 100

        total = 'C' * centena

        decimal = decimal % 100 

    if decimal <= 3:

        total += 'I' * decimal

    elif decimal == 5:

        total += 'V'

    elif decimal == 10:

        total += "X"

    return total


class TestDecimalToRoman(unittest.TestCase):

    def test_uno(self):

        # pre condicion

        ### NO HAY ###

        # proceso

        resultado = decimal_to_roman(1)

        # verificacion

        self.assertEqual(resultado, 'I')


    def test_diez(self):

        resultado = decimal_to_roman(10)

        self.assertEqual(resultado, 'X')

    def test_cinco(self):

        resultado = decimal_to_roman(5)

        self.assertEqual(resultado, 'V')



    def test_dos(self):

        resultado = decimal_to_roman(2)

        self.assertEqual(resultado, 'II')


    def test_tres(self):

        resultado = decimal_to_roman(3)

        self.assertEqual(resultado, 'III')


    def test_cien(self):

        resultado = decimal_to_roman(100)

        self.assertEqual(resultado, 'C')


    def test_ciento_uno(self):

        resultado = decimal_to_roman(101)

        self.assertEqual(resultado, 'CI')


    def test_ciento_tres(self):

        resultado = decimal_to_roman(103)

        self.assertEqual(resultado, 'CIII')


    def test_ciento_cinco(self):

        resultado = decimal_to_roman(105)

        self.assertEqual(resultado, 'CV')


    def test_ciento_diez(self):

        resultado = decimal_to_roman(110)

        self.assertEqual(resultado, 'CX')

    def test_docientos_tres(self):

        resultado = decimal_to_roman(203)

        self.assertEqual(resultado, 'CCIII')



if __name__ == '__main__':

    unittest.main()

"""
""""
import unittest

def decimal_a_romano(decimal):
    if decimal < 1 or decimal > 1000:
        return ""

    valores = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), 
              ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), 
              ("V", 5), ("IV", 4), ("I", 1)]

    romano = ""
    for letra, valor in valores:
        while decimal >= valor:
            decimal -= valor
            romano += letra

    return romano

class TestDecimalRoman(unittest.TestCase):
    def test_1(self):
        resultado = decimal_a_romano(1)
        self.assertEqual(resultado, "I")

    def test_4(self):
        resultado = decimal_a_romano(4)
        self.assertEqual(resultado, "IV")

    def test_9(self):
        resultado = decimal_a_romano(9)
        self.assertEqual(resultado, "IX")

    def test_40(self):
        resultado = decimal_a_romano(40)
        self.assertEqual(resultado, "XL")

    def test_90(self):
        resultado = decimal_a_romano(90)
        self.assertEqual(resultado, "XC")

    def test_400(self):
        resultado = decimal_a_romano(400)
        self.assertEqual(resultado, "CD")

    def test_900(self):
        resultado = decimal_a_romano(900)
        self.assertEqual(resultado, "CM")

    def test_1000(self):
        resultado = decimal_a_romano(1000)
        self.assertEqual(resultado, "M")

if __name__ == '__main__':
    unittest.main()
"""

#ROMANOS 

import unittest


def decimal_a_romano(decimal):

    if decimal <= 3:
    
        return "I" * decimal

    elif decimal == 4:
 
        return "IV"
    
    elif decimal == 5:

        return "V"

    elif decimal == 10:

        return "X"

    elif decimal >10 and decimal <= 13:

        return "X", "I" * decimal-10

    elif decimal == 14:

        return "XIV"

    elif decimal >=15 and decimal <= 18:

        return "XV", "I" * decimal-15
    
    elif decimal == 19:

        return "IX"
    elif decimal == 20:
        
        return "XX"
    


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
