import random

class RandomAgent:
    def act(self):
        return random.choice(["UP", "DOWN", "LEFT", "RIGHT"])