# forge/registry/agent_registry.py

class AgentRegistry:

    def __init__(self):

        self.agents = {}

    def register(self, agent):

        self.agents[agent.name] = agent

    def unregister(self, name):

        if name in self.agents:

            del self.agents[name]

    def get(self, name):

        return self.agents.get(name)

    def exists(self, name):

        return name in self.agents

    def list_agents(self):

        return list(self.agents.keys())