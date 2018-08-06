'''
unittest.py

Simple example of a unit test.

Taken from unittest documentation.
https://docs.python.org/3/library/unittest.html
and this tutorial
https://dzone.com/articles/python-3-testing-an-intro-to-unittest
'''
import unittest

class SimplisticTest(unittest.TestCase):

    def test(self):
        a = 'a'
        b = 'a'
        self.assertEqual(a, b)
 
if __name__ == '__main__':
    unittest.main()