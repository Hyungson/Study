import sys
from collections import deque

#sys.stdin = open("input.txt","rt")
num_node, num_line, start  = map(int,sys.stdin.readline().split())


def makeGraph(num_node=num_node,num_line=num_line):
    graph = {node +1 : [] for node in range(num_node)}
    for _ in range(num_line):
        
        i, j = map(int,sys.stdin.readline().split())
        graph[i].append(j)


    for i in range(1,num_node+1):
        for j in range(1,num_node+1):
            if i in graph[j]:
                graph[i].append(j)

        graph[i] = list(set(graph[i]))
        graph[i] = sorted(graph[i])
    
    return graph



def dfs(start_node): # stack
    visited=[]
    stack = [start_node]
    while len(stack)!= 0: #len(visited) != num_node:
        
        n = stack.pop()
        
        if n not in visited:
            visited.append(n)
            
            for i in range(len(graph[n]),0,-1):
                stack.append(graph[n][i-1])
       
    return visited

def bfs(start_node): # queue
    visited = [start_node]
    queue = deque()
    queue.append(start_node)
    while len(queue)!=0:  #len(visited) != num_node:
        n = queue.popleft()
        for connected_node in graph[n]:
            if connected_node not in visited:
                visited.append(connected_node)
                queue.append(connected_node)
        #print(queue)

    return visited

graph = makeGraph()


for j in dfs(start):
    print(j,end=' ')

print()
for j in bfs(start):
    print(j,end=' ')


