#include <iostream>
#include <vector>

using namespace std;

class Graph {
    private : vector<vector<int>> adjacencyMatrix;
    private : int numNodes;

    public : Graph(int n) : numNodes(n) {
        // Init graph with n nodes. Construct n by n matrix filled with zeros.
        this->adjacencyMatrix = vector<vector<int> >(n, vector<int>(n));
        cout << "this is called\n";
    }

    // M E M B E R S
    void printGraph() {
        for (int i=0; i < adjacencyMatrix.size(); i++) {
            // using simple for loop rather than range based because its annyoing w/o the iterator
            cout << "[";
            for (int j=0; j < adjacencyMatrix[i].size(); j++) {
                if (j+1 != adjacencyMatrix[i].size()) {
                    cout << adjacencyMatrix[i][j] << ", ";
                }
                else if (j+1 == adjacencyMatrix[i].size()) {
                    cout << adjacencyMatrix[i][j] << "]\n";
                }
            }
        }
    }

    // Todo implement these methods:
    void addVertex() {
        /* for now im simply going to append a node to the graph.
        for example say you have 3 nodes in the graph and you need to
        add another, you simply call this function and it appends a node
        (row) to the adjacency matrix.

        note when we add a row we must also extend all existing rows by 1
        */
       this->numNodes++;
       this->adjacencyMatrix.push_back(vector<int>(numNodes, 0));
       for (int i=0; i<adjacencyMatrix.size(); i++) {
        // push a 0 to each node's edge list save the row we just added.
        if (i != numNodes - 1) 
        {
            adjacencyMatrix[i].push_back(0);
        }
       }

    }
    void addEdge(int nodeIdx, int trgtIdx) {
        // check node and target within bounds
        if (nodeIdx, trgtIdx >= 0 && nodeIdx, trgtIdx < this->numNodes)
        {
            this->adjacencyMatrix[nodeIdx][trgtIdx] = 1;
        }
        else 
        {   
            cout << "Node: " << nodeIdx
            << " and/or Target: " << trgtIdx << " out of bounds\n"; 
        }
    }

    void dfs(int startNode) {}
};

int main() {
    Graph g = Graph(3);
    g.printGraph();
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 3);
    
    cout << "after adding edges\n";
    g.printGraph();
    g.addVertex();
    g.addEdge(2, 3);
    cout << "now adding edge (2,3) works\n";
    g.addVertex();
    g.addVertex();
    g.addVertex();
    g.addEdge(1, 6);
    g.printGraph();
}