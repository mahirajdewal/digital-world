from world import GridWorld
from agent import RandomAgent

world = GridWorld(size = 5, start = (0,0), goal = (4, 4))
agent = RandomAgent()

while not world.done:
    action = agent.act()
    world.step(action)
    print("Agent Position : ", world.agent_pos)