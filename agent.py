class Agent:
    def __init__(self, name):
        self.name = name

    def run(self, message):
        return f"{self.name} received: {message}"
