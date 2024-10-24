#include <iostream>
#include <vector>
#include <stack>
#include <map>

using namespace std;

class Graph {
    private : vector<vector<int> > adjacencyMatrix;
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
        if (nodeIdx >= 0 && trgtIdx >= 0 && nodeIdx < this->numNodes && trgtIdx < this->numNodes)
        {
            this->adjacencyMatrix[nodeIdx][trgtIdx] = 1;
        }
        else 
        {   
            cout << "Node: " << nodeIdx
            << " and/or Target: " << trgtIdx << " out of bounds\n"; 
        }
    }

    void adjacentEdges() {}

    void dfs(int startNode, stack<int>& explore, map<int,bool>& discovered) {
        if (!(startNode >= 0 && startNode < this->adjacencyMatrix.size()))
        {
            cout << "start node out of bounds\n";
            return;
        }

        // base case for recursion? startNode exists in stack
        // start with iterative solution
        discovered[startNode] = true;
        explore.push(startNode);
        while (!explore.empty())
        {
            int curr = explore.top();

            // remove it from stack
            explore.pop();

            // find all nodes adjacent to startNode and add them to the stack
            for (int i=0; i < this->numNodes; i++) {
                if (this->adjacencyMatrix[curr][i] == 1 && !discovered[i])
                {
                    // nextNode exists and not yet discovered.
                    explore.push(i);
                    discovered[i] = true;
                }
            }

            cout << "node: " << curr << " discovered: " << (discovered[curr] ? "true" : "false") << endl;
        }
    }
};

int main() {
    // We will construct the graph depicted in funGraph.png
    Graph g = Graph(6);

    // Since the graph begins at 1 we shift all pictured node numbers left by 1,
    // node 1 becomes node 0 etc.

    // build the edges
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 5);
    g.addEdge(2, 3);
    g.addEdge(3, 4);
    g.printGraph();
    stack<int> explored;
    map<int,bool> discovered;
    g.dfs(0, explored, discovered);
}