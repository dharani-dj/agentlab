class CalculatorTool:
	name = "calculator"
	description = "Performs basic arithmetic calculations"

	def run(self, expression):
		return eval(expression)
