'''
Created on Feb 16, 2015

@author: Arthur
'''
import re

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Graph:
    def __init__(self):
        self.nodelist = []

    def DeserializationOnOJ(self, srlztnOnOJ):
        if srlztnOnOJ == "{}":
            return True

        paraValid = (srlztnOnOJ.startswith("{") and srlztnOnOJ.endswith("}"))
        if not paraValid:
            return False

        if re.search(r"^{#.*|.*##.*", srlztnOnOJ):
            return False

        datalist = srlztnOnOJ[1:-1].split('#')

        for item in datalist:
            itemdata = item.split(',')
            gn = self.getNodeByLable(itemdata[0])
            if gn is None:
                gn = UndirectedGraphNode(itemdata[0])
                self.nodelist.append(gn)

            for neighborLable in itemdata[1:]:
                nbnode = self.getNodeByLable(neighborLable)
                if nbnode is None:
                    nbnode = UndirectedGraphNode(neighborLable)
                    self.nodelist.append(nbnode)
                gn.neighbors.append(nbnode)

        return True

    def getNodeByLable(self, label):
        for node in self.nodelist:
            if node.label == label:
                return node
        return None

    def SerializationOnOJ(self):
        if len(self.nodelist) == 0:
            return "{}"

        srlztnOnOJ = "{"

        queue = [self.nodelist[0]]
        while queue:
            gn = queue.pop(0)
            if gn is None:
                raise UserWarning("A Graph's nodelist include a NONE node! None is not allowed")
                continue

            if re.search(r"^{{{:}|#{:}".format(gn.label, gn.label), srlztnOnOJ):
                continue

            srlztnOnOJ += str(gn.label)
            for neighbor in gn.neighbors:
                queue.append(neighbor)
                srlztnOnOJ += ',' + str(neighbor.label)
            srlztnOnOJ += '#'

        result = re.sub(r"#*\Z", r"", srlztnOnOJ)
        return result + '}'

