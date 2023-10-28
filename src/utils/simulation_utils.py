```python
import random
from typing import List

class AI_Agent:
    def __init__(self, id: int):
        self.id = id
        self.status = "idle"

    def collaborate(self):
        self.status = "collaborating"

class Simulation:
    def __init__(self, num_agents: int):
        self.agents = [AI_Agent(i) for i in range(num_agents)]

    def start_collaboration(self):
        collaborating_agents = random.sample(self.agents, 10)
        for agent in collaborating_agents:
            agent.collaborate()

    def get_agent_statuses(self) -> List[str]:
        return [agent.status for agent in self.agents]
```