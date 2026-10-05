import ast
import operator


class CalculatorTool:
    name = "calculator"
    description = "Performs basic arithmetic calculations."

    OPERATORS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
    }

    def run(self, expression):
        tree = ast.parse(expression, mode="eval")
        return self._evaluate(tree.body)

    def _evaluate(self, node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in self.OPERATORS:
            left = self._evaluate(node.left)
            right = self._evaluate(node.right)
            return self.OPERATORS[type(node.op)](left, right)

        raise ValueError("Unsupported expression")
class ToolRegistry:
    def __init__(self):
        self._tools = {}

    def register(self, tool):
        self._tools[tool.name] = tool

    def get(self, name):
        if name not in self._tools:
            raise ValueError(f"Unknown tool: {name}")

        return self._tools[name]

    def list_tools(self):
        return list(self._tools.keys())
