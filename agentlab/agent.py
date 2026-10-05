class Agent:
	def __init__(self,name = "Agentlab"):
		self.name= name
	def run(self,task):
		print(f"{self.name} received task:")
		print(task)

