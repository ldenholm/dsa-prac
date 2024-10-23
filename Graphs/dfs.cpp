#include <iostream>
#include <vector>

using namespace std;

class Graph {
    private : vector<vector<int>> adjacencyMatrix;
    private : int numNodes;

    public : Graph(int n) : numNodes(n) {
        // Init graph with n nodes. Construct n by n matrix filled with zeros.
        this->adjacencyMatrix = vector<vector<int> >(n, vector<int>(n));
    }

    // M E M B E R S
    void printGraph() {
        int edgeCount = this->numNodes;
        for (int i=0; i < adjacencyMatrix.size(); i++) {
            // using simple for loop rather than range based because its annyoing w/o the iterator
            cout << "[";
            for (int j=0; j < edgeCount; j++) {
                if (j+1 != edgeCount) {
                    cout << adjacencyMatrix[i][j] << ", ";
                }
                else if (j+1 == edgeCount) {
                    cout << adjacencyMatrix[i][j] << "]\n";
                }
            }
        }
    }

    // Todo implement these methods:
    void addEdge(int node, int target) {}
    void dfs(int startNode) {}
};

int main() {
    Graph g = Graph(3);
    g.printGraph();
}