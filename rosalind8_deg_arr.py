'''

Author: Jeremy Muriungi
CS 473-1 Algorithms
Dr. Kent Jones

Rosalind 8 Degree Array:
https://rosalind.info/problems/deg/?class=934

Resources used:
https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
https://www.freecodecamp.org/news/python-string-format-python-s-print-format-example/

Last Modified 09/22/2022

'''

# open file with dataset
# f = open('rosalind_test_file.txt', 'r')
with open('rosalind_ddeg.txt', 'r') as f:
    lines = [line.rstrip() for line in f]       # rstrip removes new line chars

nm = lines[0].split(" ")
# get number of vertices and edges from first line
vertices = int(nm[0])
edges = int(nm[1])
# create 2D degree list
# degree_list = [[ [0] * vertices] * vertices]
degree_list = [[]for j in range(vertices+1)]
degree_string = ""
# populate degree list with vertices and their corresponding edges
for i in range(1, edges+1):
    v1 = int(lines[i].split()[0])
    v2 = int(lines[i].split()[1])
    #print(v1, v2)
    # if (i+1 == v1 for b in range(1,8) ):
    # if v1 == 50 or v2 == 50:
    #     print(v1, v2)
    degree_list[v1].append(v2)
    degree_list[v2].append(v1)
for i in range(1, vertices+1):
    degree_string += str(len(degree_list[i])) + " "
print(degree_string)
    # print(f"{len(degree_list[i])} ")
    # print("{} ".format(len(degree_list[i])))
