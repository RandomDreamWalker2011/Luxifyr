# setup.py
Tokens = {}


class Token:
    name = None

    def __init__(self, object_type, value):
        self.type = object_type
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
        tokens = file.split(";")
        for token in tokens:
            print(token)
        return tokens

    @staticmethod
    def breakdown(token):
        """
        token = token.strip()
        if token[:2] == "/*" and token[len(token) - 2:] == "*/":
            return "Comment found"""""
        comment_start = []
        function_runs = {}
        if token.startswith("log"):
            if token.endswith(";"):
                print(token[3:1])

    def log(self, input_operation):
        print(input_operation)
