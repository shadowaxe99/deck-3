```python
import time
from src.utils.simulation_utils import AI_Agent

class RealtimeSimulation:
    def __init__(self, num_agents):
        self.num_agents = num_agents
        self.agents = [AI_Agent() for _ in range(num_agents)]

    def start_simulation(self):
        for agent in self.agents:
            agent.start()

    def stop_simulation(self):
        for agent in self.agents:
            agent.stop()

    def display_simulation(self):
        self.start_simulation()
        time.sleep(10)  # Display the simulation for 10 seconds
        self.stop_simulation()

if __name__ == "__main__":
    simulation = RealtimeSimulation(10)
    simulation.display_simulation()
```