# -*- coding: utf-8 -*-

"""
test_pylint.py - Analyze Python code quality with pylint

This module contains a unit test to check
the code quality of the project using pylint.

Copyright (c) 2024 Suriyaa Sundararuban
Copyright (c) 2024 Elara Aerospace team
"""

import unittest
from pylint.lint import Run

class TestCodeQuality(unittest.TestCase):
    """
    Unit tests for analyzing Python code quality with pylint.
    """

    def test_pylint_conformance(self):
        """
        Test the project's code conformance to pylint standards.
        """
        pylint_output = Run(['src', '--disable=R,C'], exit=False)
        pylint_stdout = pylint_output.linter.reporter.out.getvalue()
        pylint_stderr = pylint_output.linter.reporter.err.getvalue()

        with open('logs/pylint_report.txt', 'w', encoding='utf-8') as report_file:
            report_file.write(pylint_stdout)

        print(pylint_stdout)
        print(pylint_stderr)

        self.assertNotIn('error', pylint_stdout.lower(), "Pylint found errors")
        self.assertNotIn('fatal', pylint_stdout.lower(), "Pylint found fatal errors")

if __name__ == '__main__':
    unittest.main()
