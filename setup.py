# setup.py


class LuxifyrInterpreter:
    def __init__(self, ):
        self.variables = {}

    @staticmethod
    def run(file):
        tokens = file.splitlines("\n")
        for token in tokens:
            print(token)
            
    @staticmethod
    def breakdown(tokens):
        for token in tokens:
            starts = []
            # mainfunc = []
            for char in token:
                if char == ":":
                    if starts[0] or starts[1]:
                        starts.append(char)
                    elif starts[3]:
                        pass
