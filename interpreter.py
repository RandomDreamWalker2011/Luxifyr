# INTERPRETER
from setup import LuxifyrInterpreter as LuxI, Tokens
interpreter = LuxI()


file_path = 'entry.lux'

try:
    with open(file_path, 'r') as file:
        # Read the entire content
        content = file.read()
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")

interpreter = interpreter.run(content)
if interpreter is not None:
    pass
