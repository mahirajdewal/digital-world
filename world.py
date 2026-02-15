class GridWorld:
    def __init__(self, size, start, goal):
        self.size = size
        self.agent_pos = start
        self.goal_pos = goal
        self.done = False

    def step(self, action):
        if self.done:
            return
        
        x, y = self.agent_pos

        if action == "UP":
            x = x - 1
        elif action == "DOWN":
            x = x + 1
        elif action == "LEFT":
            y = y - 1
        elif action == "RIGHT":
            y = y + 1

        # Boundary Check

        x = max(0, min(self.size - 1, x))
        y = max(0, min(self.size - 1, y))

        self.agent_pos = (x,y)

        if self.agent_pos == self.goal_pos:
            self.done = True