from src.InputInterface import InputInterface
import random


class TestInput(InputInterface):
    values = [2, "d", "s"]

    def input_string(self, message):
        return random.choice(self.values[1:])

    def input_int(self, message):
        return self.values[0]
