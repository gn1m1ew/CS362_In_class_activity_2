# import unittest
# import fibonacci

# class test(unittest.TestCase):
#     def testFibonacci1(self):
#         self.assertEqual(fibonacci.Fibonacci(0), 0)
#     def testFibonacci2(self):
#         self.assertEqual(fibonacci.Fibonacci(1), 1)
#     def testFibonacci3(self):
#         self.assertEqual(fibonacci.Fibonacci(4), 3)
#     def testFibonacci4(self):
#         self.assertEqual(fibonacci.Fibonacci(-1), None)
#     def testFactorial1(self):
#         self.assertEqual(fibonacci.recur_factorial(0), None)
#     def testFactorial2(self):
#         self.assertEqual(fibonacci.recur_factorial(2), 2)
#     def testFactorial3(self):
#         self.assertEqual(fibonacci.recur_factorial(6), 720)
#     def testFactorial4(self):
#         self.assertEqual(fibonacci.recur_factorial(-1), None)

# # def test_Fib_answer():
# #     assert fibonacci.Fibonacci(8) == 13
# #     assert fibonacci.Fibonacci(0) == 0
# #     assert fibonacci.Fibonacci(1) == 1
# #     assert fibonacci.Fibonacci(4) == 3
# #     assert fibonacci.Fibonacci(-1) == None

# # def test_Fac_answer():
# #     assert fibonacci.recur_factorial(3) == 6
# #     assert fibonacci.recur_factorial(1) == 1
# #     assert fibonacci.recur_factorial(0) == None

# if __name__ == '__main__':
#     unittest.main(verbosity=2)
import unittest
import pytest
import sys
from fibonacci import recur_factorial, Fibonacci

class TestFibbonaci(unittest.TestCase):
    def test_fib1(self):
        self.assertEqual(Fibonacci(1), 1)
    def test_fib2(self):
        self.assertEqual(Fibonacci(2), 1)
    def test_fib3(self):
        self.assertEqual(Fibonacci(3), 2)
    def test_fib4(self):
        self.assertEqual(Fibonacci(4), 3)
    def test_fib5(self):
        self.assertEqual(Fibonacci(5), 5)
    def test_fibNeg(self):
        self.assertEqual(Fibonacci(-6), None)
    def test_fac1(self):
        self.assertEqual(recur_factorial(1), 1)
    def test_fac2(self):
        self.assertEqual(recur_factorial(2), 2)
    def test_fac3(self):
        self.assertEqual(recur_factorial(3), 6)
    def test_fac4(self):
        self.assertEqual(recur_factorial(4), 24)
    def test_fac5(self):
        self.assertEqual(recur_factorial(5), 120)
    def test_facNeg(self):
        self.assertEqual(recur_factorial(-6), None)


if __name__ == '__main__':
    unittest.main(verbosity=2)