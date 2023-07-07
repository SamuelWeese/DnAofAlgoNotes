# Graph Theory and

transpose of A = -A

1 -> 2 -> 3 -> 4
4 -> 1
A =
[
 0 1 0-1
-1 0 1 0
 0-1 0 1
 1 0-1 0
] (this is adjacency matrix from discrete stuctures, HW 3)
(1 REPRESENTS connection from current node to other index, -1 represents index connecting to current node)

Can also be stored as a list

1: 2
2: 3
3: 4
4: 1

# Search algorithm

Non deterministic, is random
for a large enough tree, n searchs will result in n different lists yielded on average
(basically a binomial trial to recreate 2 lists)
## Depth First Search
1. Explore every node you can
2. then back track across each node, trying 1 then 2
stack version
O(n) is W(n) for DFS
## Breadth First Search
1. Explore all neighbors
2. Pick a neighbor and explore all neighbors which are not explored
3. Forced to store data
que version
O(n) is W(n) for BFS
