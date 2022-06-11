import numpy as np
import math


def NT(start, end, dist_mat):
    maxNode = len(dist_mat)
    Visited = np.zeros(maxNode)
    Distance = math.inf*np.ones(maxNode)
    Visited[start-1] = 1
    Distance[start-1] = 0

    for i in range(maxNode):
        if dist_mat[start-1][i] < math.inf:
            Distance[i] = dist_mat[start-1][i]

    for i in range(maxNode):
        minDist = math.inf
        for j in range(maxNode):
            if Visited[j] == 0 and Distance[j]<minDist:
                unvisitedNearest = j+1
                minDist = Distance[j]
        if minDist == math.inf:
            break
        Visited[unvisitedNearest-1] = 1
        for j in range(maxNode):
            if dist_mat[unvisitedNearest-1][j] < math.inf and Visited[j] == 0:
                if Distance[j] > dist_mat[unvisitedNearest-1][j] + Distance[unvisitedNearest-1]:
                    Distance[j] = dist_mat[unvisitedNearest-1][j] + Distance[unvisitedNearest-1]
    if Distance[end-1] == math.inf:
        print('NO')
    else:
        print('YES')
        print(Distance[end-1])
    return


n = list(map(int, input().rstrip().split()))
edges = []
maxNode = 0
for i in range(n[0]):
    l = list(map(int, input().rstrip().split()))
    edges.append(l)
    if maxNode < max(l[0],l[2]):
        maxNode = max(l[0],l[2])

dist_mat = math.inf*np.ones([maxNode,maxNode])

for i in range(maxNode):
    dist_mat[i][i] = 0
for l in edges:
    if dist_mat[l[0]-1][l[2]-1] > l[1]:
        dist_mat[l[0]-1][l[2]-1] = l[1]
    if dist_mat[l[2]-1][l[0]-1] > l[1]:
        dist_mat[l[2]-1][l[0]-1] = l[1]

NT(n[1], n[2], dist_mat)
