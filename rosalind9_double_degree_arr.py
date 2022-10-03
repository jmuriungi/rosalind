'''

Author: Jeremy Muriungi
CS 473-1 Algorithms
Dr. Kent Jones

Rosalind 8 Double-Degree Array:
https://rosalind.info/problems/ddeg/?class=934

Resources used:


Last Modified 09/22/2022

'''

# open file with dataset
with open('rosalind_ddeg.txt', 'r') as f:
    lines = [line.rstrip() for line in f]

num_of_vertices_n_edges = lines[0].split(" ")
vertices = int(num_of_vertices_n_edges[0])
edges = int(num_of_vertices_n_edges[1])

# 2D degree list
degree_list = [[] for i in range(vertices)]
# list of sum of degrees of a vertice's neighbors
degree_sum = [0] * vertices

degree_string = ""
sum_string = ""
# populate degree list with vertice's neighbors
for i in range(edges):
    v1 = int(lines[i+1].split(" ")[0])
    v2 = int(lines[i+1].split(" ")[1])
    #print(v1, v2)
    degree_list[v1-1].append(v2)
    degree_list[v2-1].append(v1)
for i in range(vertices):
    degree_string += str(len(degree_list[i])) + " "
# print(degree_string)
# populate degree sum
for i in range(vertices):
    if len(degree_list[i]) == 0:
        degree_sum[i] = 0
        sum_string += str(degree_sum[i]) + " "
    else:
        for j in range(len(degree_list[i])):
            degree_sum[i] += len(degree_list[(degree_list[i][j])-1]) # sum of length of inner lists
        sum_string += str(degree_sum[i]) + " "
print(sum_string)