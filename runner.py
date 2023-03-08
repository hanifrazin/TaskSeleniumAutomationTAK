import unittest
from unittest.suite import TestSuite
import RegisterUser, Login

if __name__ == '__main__':
    # create test suite from classes
    suite = TestSuite()
    # panggil test
    tests = unittest.TestLoader()
    # menambahkan test ke suite
    suite.addTests(tests.loadTestsFromModule(RegisterUser))
    suite.addTests(tests.loadTestsFromModule(Login))

    #run test suite
    runner = unittest.TextTestRunner()
    runner.run(suite)
