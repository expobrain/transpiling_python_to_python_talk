import ast
import astor

tree = ast.parse('print("Hello, World!")')
# Module(
#     body=[
#         Expr(
#             value=Call(func=Name(id='print'),
#             args=[Str(s='Hello, World!')],
#             keywords=[])
#         )
#     ]
# )

code = astor.code_gen.to_source(tree)
# "print('Hello, World!')\n"
