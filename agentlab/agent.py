from agentlab.tools import CalculatorTool, ToolRegistry


class Agent:
    def __init__(self, name="AgentLab"):
        self.name = name

        self.tools = ToolRegistry()
        self.tools.register(CalculatorTool())

    def run(self, task):
        print(f"{self.name} received task:")
        print(task)

        calculator = self.tools.get("calculator")

        result = calculator.run("25 * 4")

        print(f"Tool result: {result}")
