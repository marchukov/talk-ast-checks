import ast

with open("good_code.py") as source:
    print(ast.dump(ast.parse(source.read())))
