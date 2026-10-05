from agentlab.tools import CalculatorTool


class Agent:
    def __init__(self, name="AgentLab"):
        self.name = name
        self.tools = {
            "calculator": CalculatorTool()
        }

    def run(self, task):
        print(f"{self.name} received task:")
        print(task)

        result = self.tools["calculator"].run("25 * 4")

        print(f"Tool result: {result}")
