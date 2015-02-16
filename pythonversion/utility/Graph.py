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

        self.nodelist = []
        for item in datalist:
            itemdata = item.split(',')
            gn = UndirectedGraphNode(itemdata[0])
            for neighbor in itemdata[1:]:
                gn.neighbors.append(neighbor)
            self.nodelist.append(gn)

        return True

    def SerializationOnOJ(self):
        if self.nodelist == None:
            return "{}"

        srlztnOnOJ = "{"
        for gn in self.nodelist:
            if gn is None:
                # maybe we can raise an exception
                continue
            srlztnOnOJ += str(gn.label)
            for neighbor in gn.neighbors:
                srlztnOnOJ += ',' + str(neighbor)
            srlztnOnOJ += '#'

        result = re.sub(r"#*\Z", r"", srlztnOnOJ)
        return result + '}'

