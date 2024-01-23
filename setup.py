# setup.py
Tokens = {}


class Token:
    name = None

    def __init__(self, type, value):
        self.type = type
        self.value = value
        self.variable = False

    def set_variable(self, name):
        self.name = name
        self.variable = True


class LuxifyrInterpreter:
    def __init__(self):
        self.variables = {}

    @staticmethod
    def run(file):
        tokens = file.split()
        for token in tokens:
            print(token)

    @staticmethod
    def breakdown(tokens):
        pass
