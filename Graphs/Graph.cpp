#include <iostream>
#include <vector>
#include <stack>
#include <map>
#include <queue>
#include "Graph.h"

using namespace std;

    Graph::Graph(int n) : numNodes(n) {
        // Init graph with n nodes. Construct n by n matrix filled with zeros.
        this->adjacencyMatrix = vector<vector<int> >(n, vector<int>(n));
        cout << "this is called\n";
    }

    // M E M B E R S
    void Graph::printGraph() {
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
    void Graph::addVertex() {
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
    void Graph::addEdge(int nodeIdx, int trgtIdx) {
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

    void Graph::dfs(int startNode, stack<int>& explore, map<int,bool>& discovered) {
        if (!(startNode >= 0 && startNode < this->adjacencyMatrix.size()))
        {
            cout << "start node out of bounds\n";
            return;
        }
        
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

            cout << "DFS: node: " << curr << " discovered: " << (discovered[curr] ? "true" : "false") << endl;
        }
    }

    void Graph::bfs(int startNode, queue<int>& explore, map<int,bool>& discovered) {
        // the difference here is we use a FIFO exploration queue.
        if (!(startNode >= 0 && startNode < this->adjacencyMatrix.size()))
        {
            cout << "start node out of bounds\n";
            return;
        }
        discovered[startNode] = true;
        explore.push(startNode);
        while (!explore.empty())
        {
            // find edges for node at front of queue
            int curr = explore.front();
            // since we are exploring curr we remove it from queue
            explore.pop();
            for (int i=0; i<this->adjacencyMatrix.size(); i++) {
                if (this->adjacencyMatrix[curr][i] == 1 && !discovered[i])
                {
                    // add node to the queue to be explored
                    explore.push(i);
                    discovered[i] = true;
                }
            }
            cout << "BFS: node: " << curr << " discovered: " << (discovered[curr] ? "true" : "false") << endl;
        }
    }