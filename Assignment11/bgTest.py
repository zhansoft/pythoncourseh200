from bestgraph import Graph

def main():
    print("Testing code below")
    print("="*30)

    givenNodes = [1, 2, 3, 4]

    givenEdges = [(1, 2), (1, 3), (3, 4)]

    g = Graph(givenNodes)
    print(g)

    print("Testing adding original edges")
    print("=" * 10)
    for e in givenEdges:
        result = g.add_edge(e)
        if result == -1:
            print("Adding edges " + str(e) + " should have returned 1. Returned -1")
    print(g)
    print("=" * 10 + "\n")

    print("Testing Add Node")

    addNodes = [1, 5, 6, 7]
    results = [-1, 1, 1, 1]

    print("=" * 10)
    for i in range(len(addNodes)):
        toAdd = addNodes[i]
        correct = results[i]
        result = g.add_node(toAdd)
        if result != correct:
            print("Adding nodes " + str(toAdd) + " should have returned " + str(-1 * result) + ". Returned " + str(result))
    print(g)
    print("=" * 10 + "\n")


    print("Testing Add Edge")

    addEdges = [(1, 2), (2, 5), (3, 2), (2, 7), (7, 2)]
    addResults = [-1, 1, 1, 1, 1]

    print("=" * 10)
    for i in range(len(addEdges)):
        toAdd = addEdges[i]
        correct = addResults[i]
        result = g.add_edge(toAdd)
        if result != correct:
            print("Adding edges " + str(toAdd) + " should have returned " + str(-1 * result) + ". Returned " + str(result))
    print(g)
    print("=" * 10 + "\n")

    # FIXME: This does not test if you delete nodes and edges correctly. If you want to ensure it works, you need to write your own tests (not required for points, but we will test ourselves)

    print("Testing Del Edge")
    delEdges = [(1, 2), (2, 5), (3, 2), (2, 7), (7, 2)]
    print("=" * 10)
    for i in range(len(addEdges)):
        g.del_edge(delEdges[i])
    print(g)
    print("=" * 10 + "\n")

    print("Testing Del Node")
    delNodes = [5, 6, 7]
    print("=" * 10)
    for i in range(len(delNodes)):
        g.del_node(delNodes[i])
    print(g)
    print("=" * 10 + "\n")

    print("Testing the Matrix thingy")
    print(g.reachable((1,3)))
    print("=" * 10 + "\n")
    


if __name__ == "__main__":
        main()