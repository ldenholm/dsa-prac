#ifndef GRAPH_H
#define GRAPH_H

#include <vector>
#include <stack>
#include <map>
#include <queue>

using namespace std;

class Graph {
    vector<vector<int> > adjacencyMatrix;
    int numNodes;
    
    public:
        Graph(int n);
        void printGraph();
        void addVertex();
        void addEdge(int nodeIdx, int trgtIdx);
        void dfs(int startNode, stack<int>& explore, map<int,bool>& discovered);
        void bfs(int startNode, queue<int>& explore, map<int,bool>& discovered);
};

#endif