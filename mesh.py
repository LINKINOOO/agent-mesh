class Mesh:
    def __init__(self):
        self.agents = {}
        self.connections = {}

    def add_agent(self, agent):
        self.agents[agent.name] = agent

    def connect(self, source, target):
        if source not in self.connections:
            self.connections[source] = []

        self.connections[source].append(target)

    def send(self, source, message):
        targets = self.connections.get(source, [])

        results = []

        for target in targets:
            agent = self.agents[target]
            result = agent.run(message)
            results.append(result)

        return results
