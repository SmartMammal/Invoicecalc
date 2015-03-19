import unittest
from invoice_calculator import divide_pay # import the function from invoice_calculator

class InvoiceCalculatorTests(unittest.TestCase):
  def testDividedFairly(self): #First example
    pay = divide_pay(360.0, {"Alice": 3.0, "Bob": 3.0, "Carol": 6.0})
    self.assertEqual(pay, {"Alice": 90.0, "Bob": 90.0, "Carol": 180.0}) # Check
  
  def testZeroHourPerson(self): #Edge case
    pay = divide_pay(360.0, {"Alice": 3.0, "Bob": 6.0, "Carol": 0.0})
    self.assertEqual(pay, {"Alice": 120.0, "Bob": 240.0, "Carol": 0.0})

  def testZeroHoursTotal(self): #Bad input cases
    with self.assertRaises(ValueError): #because you're expecting an error, you have to catch the exception
        pay = divide_pay(360.0, {"Alice": 0.0, "Bob": 0.0, "Carol": 0.0})
        
  def testNoPeople(self):
    with self.assertRaises(ValueError):
        pay = divide_pay(360.0, {})
    
if __name__ == "__main__":
    unittest.main()