# Graph Important Applications

## Using DFS and BFS

1. Testing whether graph is connected
- for both dfs and bfs, worst case is:
    - connected is O(n)
    - not connected is O(m+n)
2. Finding Shortest Paths
- dfs is a lot of work to tweak to find this
- bfs is fast, as using nodes u, v
    - covers neighbors of u, then neighbors 2 hops from u,
    - stops when it returns v
3. Computing the connected components
- similar complexity for both DFS and BFS
- A(n) is similar to W(n) as both must access every node

4. Computing the diameter
- diameter is distance between farthest pair of two nodes
- I assume breadth first search, finding the longest shortest distance
- naieve approach is O(n+m), and non-naieve is O(m+n), tho average is shortest

# Topological Sorting
DAG is directed acyclic graph
- a graph which contains no directed cycles

1->2->3->4->5->2 is directed graph
1->2->3->4 2->5 is DAG
## source and sink
Source is node with only outgoing edges
- found by following all nodes to completion
- source are all nodes not pointed to in the graph
Sink is node with only incoming edges
- found by following all nodes to completion
- sink are all nodes not pointing to another node
DAGs must have source and sink, directed graph can have but not must

# Dag usage
Task Scheduling
Example
- 1 must come before 5
- 2 must come before 3
- 4 must come before 3
- 5 must come before 3
Resulting graph
1->5
2->3
4->3
5->3
Check if resulting graph is a DAG

Order 1:
1->5->2->4->3
Order 2:
1->5->2->3->4

Order 2 is invalid due to 3->4 relationship, as 3 is before 4
# DAG traversal
- deleting sources and adding to front of list
- deleting nodes and adding to back of the list
- run dfs from source
    - for each node, mark node as explored (ref list)
    - back track as you would in dfs
    - find order of back track, this is topologically sorted list
    - order of back track, not order of visited nodes
