class GoalAgent:
    def act(self, agent_pos, goal_pos):
        x, y = agent_pos
        gx, gy = goal_pos

        actions = {
            "UP":    (x - 1, y),
            "DOWN":  (x + 1, y),
            "LEFT":  (x, y - 1),
            "RIGHT": (x, y + 1),
        }

        def manhattan_distance(pos):
            return abs(pos[0] - gx) + abs(pos[1] - gy)

        return min(actions, key=lambda a: manhattan_distance(actions[a]))
