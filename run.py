from world import GridWorld
from agents.random_agent import RandomAgent
from agents.goal_agent import GoalAgent
import time

# Choose agent here
AGENT_TYPE = "goal"  # "random" or "goal"

world = GridWorld(size = 5, start = (0,0), goal = (4, 4))

if AGENT_TYPE == "random":
    agent = RandomAgent()
elif AGENT_TYPE == "goal":
    agent = GoalAgent()
else:
    raise ValueError("Unknown agent type")

while not world.done:
    world.render()
    action = agent.act(world.agent_pos, world.goal_pos)
    world.step(action)
    time.sleep(0.3)

world.render()
print(f"Finished using {AGENT_TYPE} agent")