"""
Name:
Surname:
ID:
"""

class DiGraphAsAdjacencyMatrix:
    def __init__(self):
        self.__nodes = list()
        self.__matrix = list()

    def __len__(self):
        """gets the number of nodes"""
        return len(self.__nodes)


    def __str__(self):
        header = "\t".join([n for n in self.__nodes])
        data = ""
        for i in range(0,len(self.__matrix)):
            data += str(self.__nodes[i]) + "\t"
            data += "\t".join([str(x) for x in self.__matrix[i]]) + "\n"

        return "\t"+ header +"\n" + data

    def insertNode(self, node):
        #add the node if not there already.
        if node not in self.__nodes:
            self.__nodes.append(node)
            #add a row and a column of zeros in the matrix
            if len(self.__matrix) == 0:
                #first node
                self.__matrix = [[0]]
            else:
                N = len(self.__nodes)
                for row in self.__matrix:
                    row.append(0)
                self.__matrix.append([0 for x in range(N)])

    def insertEdge(self, node1, node2, weight):
        i = -1
        j = -1
        if node1 in self.__nodes:
            i = self.__nodes.index(node1)
        if node2 in self.__nodes:
            j = self.__nodes.index(node2)
        if i != -1 and j != -1:
            self.__matrix[i][j] = weight

    #---------------------------------------#
    # do not edit code above this line!
    #---------------------------------------#

    def getNumberOfConnectedNodes(self, mynode, modality):
        """
        modality = 1 uses only incoming edges;
        modality = 2 uses only outgoing edges;
        Print an error message and return 0 when mynode does not exist or
        when the method modality is not supported.
        """
        ret = 0
        i = -1
        if mynode in self.__nodes:
            i = self.__nodes.index(mynode)

        # if the node is present
        if i != -1:
            # outgoing edges
            if modality == 2:
                for e in range(len(self.__matrix[i])):
                    if self.__matrix[i][e] != 0:
                        ret +=1
            # incomming edges
            elif modality == 1:
                for e in range(len(self.__matrix)):
                    if self.__matrix[e][i] != 0:
                        ret +=1
            else:
                print(f"ERROR: Modality {modality} is not supported")

        else:
            print(f"ERROR: {mynode} does not exist")
        return ret


    def getAverageNumberOfEdgesPerNode(self):
        """
        returns average number of edges per nodes in the graph
        """
        edge_avg = []
        for node in self.__nodes:
            in_e = self.getNumberOfConnectedNodes(node, 1)
            out_e = self.getNumberOfConnectedNodes(node, 2)
            edge_avg.append(in_e+out_e)

        return sum(edge_avg)/len(edge_avg)

if __name__ == "__main__":
    G = DiGraphAsAdjacencyMatrix()

    for i in range(11):
        n = "Node_{}".format(i+1)
        G.insertNode(n)

    G.insertEdge("Node_1", "Node_9", 5)
    G.insertEdge("Node_1", "Node_2", 2)
    G.insertEdge("Node_2", "Node_4", 1)
    G.insertEdge("Node_2", "Node_5", 3.5)
    G.insertEdge("Node_2", "Node_3", 2)
    G.insertEdge("Node_3", "Node_5", 2)
    G.insertEdge("Node_4", "Node_6", 1)
    G.insertEdge("Node_4", "Node_7", 2)
    G.insertEdge("Node_5", "Node_10", 3)
    G.insertEdge("Node_5", "Node_9", 1)
    G.insertEdge("Node_6", "Node_7", 1)
    G.insertEdge("Node_6", "Node_9", 2)
    G.insertEdge("Node_7", "Node_4", 2)
    G.insertEdge("Node_7", "Node_5", 1)
    G.insertEdge("Node_7", "Node_9", 3)
    G.insertEdge("Node_8", "Node_3", 4)
    G.insertEdge("Node_8", "Node_2", 7)
    G.insertEdge("Node_8", "Node_1", 7)
    G.insertEdge("Node_9", "Node_1", 5)
    G.insertEdge("Node_9", "Node_3", 4)
    G.insertEdge("Node_9", "Node_5", 1)
    G.insertEdge("Node_9", "Node_8", 1)
    G.insertEdge("Node_9", "Node_10", 4)
    G.insertEdge("Node_10", "Node_3", 3)
    G.insertEdge("Node_11", "Node_10", 1)

    print("Size is: {}".format(len(G)))
    print("\nMatrix:")
    print(G)

    #PART 1
    print("\nPART 1:\n")
    nodes = ["Node_3", "Node_7", "Node_11"]

    print("\n-> modality 1 test:")
    for n in nodes:
        n_e = G.getNumberOfConnectedNodes(n, 1)
        print(f"\t{n} has {n_e} incoming links.")

    print("\n-> modality 2 test:")
    for n in nodes:
        n_e = G.getNumberOfConnectedNodes(n, 2)
        print(f"\t{n} has {n_e} outgoing links.")

    print("\n-> invalid cases:")
    n_e = G.getNumberOfConnectedNodes("Node_27", 2)
    print(f"\tNode_27 has {n_e} outgoing links.")
    n_e = G.getNumberOfConnectedNodes("Node_27", 3)
    print(f"\tNode_27 has {n_e} outgoing links.")

    # some asserts
    assert G.getNumberOfConnectedNodes("Node_11", 1) == 0
    assert G.getNumberOfConnectedNodes("Node_4", 1) == 2
    assert G.getNumberOfConnectedNodes("Node_4", 2) == 2

    #PART 2
    print("\nPART 2:\n")
    print(f"Average number of edges per node in the graph: {G.getAverageNumberOfEdgesPerNode()}\n")

    assert G.getAverageNumberOfEdgesPerNode() == 4.545454545454546


