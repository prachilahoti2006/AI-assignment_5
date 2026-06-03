import random
import math

class TreeNode:

    def __init__(self):
        self.score = 0
        self.count = 0
        self.nodes = []

    def calculate_uct(self, parent_visits):

        if self.count == 0:
            return float('inf')

        exploitation = self.score / self.count
        exploration = math.sqrt(math.log(parent_visits) / self.count)

        return exploitation + exploration


parent = TreeNode()

for i in range(5):

    temp = TreeNode()

    temp.score = random.randint(1, 10)
    temp.count = random.randint(1, 10)

    parent.nodes.append(temp)

parent.count = sum(node.count for node in parent.nodes)

selected = max(
    parent.nodes,
    key=lambda node: node.calculate_uct(parent.count)
)

print("Best Child:")
print("Wins:", selected.score)
print("Visits:", selected.count)
