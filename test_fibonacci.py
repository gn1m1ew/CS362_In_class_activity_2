import unittest
import fibonacci

# class testFib(unittest.TestCase):
#     def testFibonacci1(self):
#         self.assertEqual(fibonacci.Fibonacci(0), 0)
#         self.assertEqual(fibonacci.Fibonacci(1), 1)
#         self.assertEqual(fibonacci.Fibonacci(4), 3)
#         self.assertEqual(fibonacci.Fibonacci(-1), None)


# class testFactorial(unittest.TestCase):
#     def testFactorial1(self):
#         # assert(fibonacci.recur_factorial(2) == 2)
#         # assert(fibonacci.recur_factorial(6) == 720)
#         # assert(fibonacci.recur_factorial(0) == 1)
#         # assert(fibonacci.recur_factorial(-1) == None)
#         self.assertEqual(fibonacci.recur_factorial(0), None)
#         self.assertEqual(fibonacci.recur_factorial(2), 2)
#         self.assertEqual(fibonacci.recur_factorial(6), 720)
#         self.assertEqual(fibonacci.recur_factorial(-1), None)

def test_Fib_answer():
    assert fibonacci.Fibonacci(8) == 13

def test_Fac_answer():
    assert fibonacci.recur_factorial(3) == 6

if __name__ == '__main__':
    unittest.main(verbosity=2)