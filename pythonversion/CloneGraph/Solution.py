# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
#
#
# OJ's undirected graph serialization:
# Nodes are labeled uniquely.
#
# We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
#
# The graph has a total of three nodes, and therefore contains three parts as separated by #.
#
# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
# Visually, the graph looks like the following:
#
#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

from utility.Graph import UndirectedGraphNode

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        self.dict = {}
        return self.createNodeBFS(node)

    def createNodeBFS(self, node):
        if node is None:
            return None

        newNode = UndirectedGraphNode(node.label)
        self.dict[node.label] = newNode

        queue = [node]
        visited = []

        while queue:
            n = queue.pop(0)
            if n.label in visited:
                continue

            for neighbor in n.neighbors:
                if neighbor.label not in self.dict:
                    nb = UndirectedGraphNode(neighbor.label)
                    self.dict[nb.label] = nb
                self.dict[n.label].neighbors.append(self.dict[neighbor.label])
                queue.append(neighbor)

            visited.append(n.label)

        return newNode

    def createNodeDFS(self, node):
        if node is None:
            return None

        newNode = UndirectedGraphNode(node.label)
        self.dict[node.label] = newNode

        for neighbor in node.neighbors:
            if neighbor.label not in self.dict:
                self.createNode(neighbor)
            newNode.neighbors.append(self.dict[neighbor.label])

        return newNode








