from django.test import TestCase
from recipeProject.calc import add,substract

class CalcTests(TestCase):
    def test_add_numbers(self):# you need start with test. 
        """Test that two numbers are added together"""
        self.assertEqual(add(3,8),11) # You call the function and put the result that you expect    
    def test_subtract_number(self):
        """Test that values are substracted and returned"""
        self.assertEqual(substract(5,11),6)