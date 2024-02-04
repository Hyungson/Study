import sys
from collections import deque

sys.stdin = open("input.txt","rt")


row,column = map(int,sys.stdin.readline().split())
# graph = []

# for _ in range(row):
#     graph.append(list(map(int, sys.stdin.readline().rstrip())))
# print(graph)
#bfs #queue

#row,column = map(int,sys.stdin.readline().split())
def makeMatrix(row,column):
    matrix = []
    for r in range(row):
        matrix.append(list(map(int, sys.stdin.readline().rstrip())))
    return matrix


matrix = makeMatrix(row,column)

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
                
            if 0 <= next_x < row and 0 <= next_y < column and matrix[next_x][next_y] == 1:
                if next_x == 0 and next_y == 0:
                    pass
                queue.append((next_x,next_y))
                matrix[next_x][next_y] = matrix[x][y] +1
                

    return matrix[row-1][column-1]

print(bfs(0,0))






