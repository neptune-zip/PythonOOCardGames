# Unit test all sub-programs with return statements.
import unittest
from src.ConsoleInput import ConsoleInput
from src.InputInterface import InputInterface


class ConsoleInputTest(unittest.TestCase, InputInterface):
    ci = ConsoleInput()

    def input_string(self):
        message = "Enter the same text here: "
        self.assertEqual(input("Enter a message to validate: "), self.ci.input_string(message))

    def input_int(self):
        message = "Enter the same number here: "
        self.assertEqual(int(input("Enter a number to validate: ")), self.ci.input_int(message))
