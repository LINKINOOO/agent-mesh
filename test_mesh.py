from agent import Agent
from mesh import Mesh


master = Agent("Master")
research = Agent("Research")


mesh = Mesh()

mesh.add_agent(master)
mesh.add_agent(research)

mesh.connect("Master", "Research")

results = mesh.send(
    "Master",
    "Research the current energy storage market."
)

print(results)
