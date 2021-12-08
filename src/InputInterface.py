from abc import ABC, abstractmethod


class InputInterface(ABC):

    @abstractmethod
    def input_string(self, message):
        pass

    @abstractmethod
    def input_int(self, message):
        pass
