class Stack:
    stack = []
    curIdx = -1
    maxNum = 0

    def __init__(self, n):
        self.maxNum = n
        self.stack = [0 for i in range(n)]

    def isEmpty(self):
        return self.curIdx == -1
    
    def isFull(self):
        return self.curIdx == self.maxNum - 1

    def push(self, value):
        self.curIdx = self.curIdx + 1
        self.stack[self.curIdx] = value

    def pop(self):
        temp = self.stack[self.curIdx]
        self.curIdx = self.curIdx - 1
        return temp

class Graph:
    nodeNum = 0
    adj_mat = [[nodeNum] for i in range(nodeNum)]
    def __init__(self, n):
        self.nodeNum = n
        self.adj_mat = [[0 for j in range(self.nodeNum)] for i in range(self.nodeNum)]
    
    def insert_edge(self, start, end):
        if((start-1) >= self.nodeNum or (end-1) >= self.nodeNum):
            print("존재하지 않는 정점입니다.")
            return
        self.adj_mat[start-1][end-1] = 1
        self.adj_mat[end-1][start-1] = 1
    
def dfs(n, v):
    s = Stack(n)
    s.push(v)
    while(s.isEmpty() != True):
        s.pop() 
        if(visited[v] == 0):
            visited[v] == 1
            for w in range(n):
                if(visited[w] == 0):
                    s.push(w)
                    parent[w] = v

    # visited[v-1] = 1
    # for w in range(n):
    #     if(adj[v-1][w] == 1 and visited[w] == 0):
    #         parent[w] = v
    #         dfs(n, adj, w+1)

n = int(input()) # 노드의 개수
visited = [0 for i in range(n)]
parent = [0 for i in range(n)]
g = Graph(n)

for i in range(g.nodeNum-1):
    s, e = map(int, input().split())
    g.insert_edge(s, e)

dfs(g.nodeNum, 1)

for i in range(1, g.nodeNum):
    print(parent[i])


