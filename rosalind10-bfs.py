'''

Author: Jeremy Muriungi
CS 473-1 Algorithms
Dr. Kent Jones

Rosalind 10 Breadth-First Search:
https://rosalind.info/problems/bfs/?class=934

Resources used:
https://www.geeksforgeeks.org/queue-in-python/

Last Modified 09/28/2022

'''

from collections import deque
from queue import Empty

# open input file
with open ('rosalind_test_file.txt', 'r') as f:
    lines = [line.rstrip() for line in f]

vertices_and_edges = lines[0].split(" ")
# get number of vertices and edges from first line
vertices = int(vertices_and_edges[0])
edges = int(vertices_and_edges[1])
# list of length of shortest path between vertex 1 to vertex i
shortest_path_len = []   
# initialize queue
bfs_queue = deque(maxlen=vertices)
# boolean list for if each vertex is visited
visited = [False] * len(bfs_queue)
count = 0
distance = 0
for vertex in range(vertices + 1):
    if visited[vertex] == False:
        count += 1
        bfs_queue.append(vertex)
        visited[vertex] = True
        distance[visited] = distance[vertex] + 1
        bfs_queue.append(vertex)
        while not bfs_queue:
            count = bfs_queue.
            for v in range 
# let vertex marked 0 be unvisited, 1 be visited
# initialize queue with starting vertex of current run
# mark starting vertex as visited; change 0 to a 1
# iterate through vertices connected to startig vertex and mark visited
# add visited vertices to queue with starting vertex
# remove front vertex from queue