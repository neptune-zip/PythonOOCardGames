from InputInterface import InputInterface


class ConsoleInput(InputInterface):

    def input_string(self, message):
        return input(message)

    def input_int(self, message):
        while True:
            try:
                myInput = int(input(message))
                return myInput
            except:
                print("+++Please enter a number+++")