import unittest

def es_primo(value):
    if value<=2: 
        return True
    i=2
    while i<value:
        if value%i ==0:
            return False
        else:
            i+=1

    return True
        
    


class TestPrimos(unittest.TestCase):
    def test_1(self):
        result = es_primo(1)
        self.assertEqual(result, True)
    
    def test_2(self):
        result = es_primo(2)
        self.assertEqual(result, True)

    def test_3(self):
        result = es_primo(3)
        self.assertEqual(result, True)

    def test_4(self):
        result = es_primo(4)
        self.assertEqual(result, False)
    
    def test_5(self):
        result = es_primo(5)
        self.assertEqual(result, True)
    
    def test_6(self):
        result = es_primo(6)
        self.assertEqual(result, False)
    
    def test_7(self):
        result = es_primo(7)
        self.assertEqual(result, True)
    
    def test_8(self):
        result = es_primo(8)
        self.assertEqual(result, False)

    def test_9(self):
        result = es_primo(9)
        self.assertEqual(result, False)

    def test_10(self):
        result = es_primo(6)
        self.assertEqual(result,False)



unittest.main()