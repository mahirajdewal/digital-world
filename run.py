from world import GridWorld
from agent import RandomAgent
import time

world = GridWorld(size = 5, start = (0,0), goal = (4, 4))
agent = RandomAgent()

while not world.done:
    world.render()
    action = agent.act()
    world.step(action)
    time.sleep(0.3)

world.render()
print("Reached Goal!")