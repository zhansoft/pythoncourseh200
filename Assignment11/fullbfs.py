from bestgraph import Graph
from queue import Queue


def bfsfull(g, node):
    #TODO: Implement function
    unvisited = g.n()
    visited = []
    q = Queue()
    q.enqueue(node)
    while unvisited:
        while not q.empty():
            vnode = q.dequeue()
            unvisited.remove(vnode)
            if vnode not in visited:
                print(vnode)
                visited.append(vnode)
                clist = g.children(vnode)
                for n in clist:
                    if n not in visited:
                        q.enqueue(n)
        # if firstnode in unvisited:
        #     q.enqueue(firstnode)
        if unvisited:
            q.enqueue(unvisited[0])


if __name__ == "__main__":
    my_graph = Graph([1, 2, 3, 4, 5, 6, 7, 8])
    elst = [(1,2), (1,3), (2, 8), (3,5), (3,4), (5,6), (6,4), (6,7)]
    for i in elst:
        my_graph.add_edge(i)
    print(my_graph.edges)
    bfsfull(my_graph, 5)