# -*- coding: utf-8 -*-

"""
test_pylint.py - Analyze Python code quality with pylint

Copyright (c) 2024 Suriyaa Sundararuban
Copyright (c) 2024 Elara Aerospace team
"""

import unittest
from pylint import epylint as lint

class TestCodeQuality(unittest.TestCase):
    def test_pylint_conformance(self):
        pylint_output = lint.py_run('src --disable=R,C', return_std=True)
        stdout, stderr = pylint_output

        pylint_stdout = stdout.getvalue()
        pylint_stderr = stderr.getvalue()

        with open('logs/pylint_report.txt', 'w') as report_file:
            report_file.write(pylint_stdout)

        print(pylint_stdout)
        print(pylint_stderr)

        self.assertNotIn('error', pylint_stdout.lower(), "Pylint found errors")
        self.assertNotIn('fatal', pylint_stdout.lower(), "Pylint found fatal errors")

if __name__ == '__main__':
    unittest.main()
