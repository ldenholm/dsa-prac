#include <iostream>
#include <vector>
#include <stack>
#include <map>
#include <queue>
#include "Graph.h"

using namespace std;

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
    
    // test bfs
    queue<int> bfs_explored;
    map<int,bool> bfs_discovered;
    g.bfs(0, bfs_explored, bfs_discovered);

    // Todo consider using unordered map to optimize lookups,
    // probably negligible gain for the size of graph im testing with.
}