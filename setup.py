# setup.py


class Luxifyr_Interpreter:
    def __init__(self, ):
        self.variables = {}

    def run(self, file):
        tokens = file.splitlines("\n")
        for token in tokens:
            print("token")
