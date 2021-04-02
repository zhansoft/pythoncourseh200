import numpy as np

class Graph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.edges = {}
        for i in self.nodes:
            self.edges[i] = []

    def add_edge(self, pair):
        start,end = pair
        if end not in self.edges[start]:
            self.edges[start].append(end)
            return 1
        else:
            return -1
    
    def add_node(self, n):
        if n not in self.nodes:
            self.nodes.append(n)
            self.edges[n] = []
            return 1
        else:
            return -1
    
    def del_node(self, n):
        if n in self.nodes:
            self.nodes.remove(n)
            del(self.edges[n])
            return 1
        else:
            return -1

    def del_edge(self, pair):
        x, y = pair
        if y in self.edges[x]:
            self.edges[x].remove(y)
            return 1
        else:
            return -1

    def reachable(self, pair):
        a = np.zeros((len(self.nodes), len(self.nodes)), dtype = int)
        for node in self.edges.keys():
            for val in self.edges[node]:
                a[node-1][val-1] = 1
        print(a)
        a = np.dot(a,a) + a
        print(a)
        a = np.dot(a,a) + a
        start, end = pair
        print(a)
        if a[start-1][end-1] == 0:
            return False
        else:
            return True
        
    def children(self,node):
        return self.edges[node]
    
    def n(self):
        return self.nodes

    def __str__(self):
        return str(self.edges)