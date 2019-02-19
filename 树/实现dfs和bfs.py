'''
实现一下深度优先搜索与广度优先搜索
'''

class method(object):
    def __init__(self,*args, **kwargs):
        self.node_neighbors =  {}
        self.visited = {}

    def add_nodes(self, node_list):
        for node in node_list:
            self.add_node(node)

    def add_node(self, node):
        if not node in self.nodes():
            self.node_neighbors[node] = []


    def add_edge(self, edge):
        u, v = edge
        if (v not in self.node_neighbors[u]) and (u not in self.node_neighbors[v]):
            self.node_neighbors[u].append(v)
            if (u != v):
                self.node_neighbors[v].append(u)

    def nodes(self):
        return self.node_neighbors.keys()     #递归DFS

    def depth_first_search(self,root=None):
        order=[]

    def dfs(node):
        self.visited[node] = True
        order.append(node)
        for n in self.node_neighbors[node]:
            if not n in self.visited:
                dfs(n)
            if root:
                dfs(root)

    #对于不连通的结点（即dfs（root）完仍是没有visit过的单独处理，再做一次dfs
         for node in self.nodes():
             if not node in self.visited:
                 dfs(node)
                 self.visited = {}
                 print order
                 return order     #非递归DFS

    def depth_first_search2(self,root=None):
        stack = []
        order = []
        #self.visited[root] = True
        def dfs():
            while stack:
                node = stack[-1]
                for n in self.node_neighbors[node]:
                    if not n in self.visited:
                        order.append(n)
                        stack.append(n)
                        self.visited[n] = True
                        break
                    else:
                        stack.pop()
                if root:
                        stack.append(root)
                        order.append(root)
                        self.visited[root]=True
                        dfs()
                for node in self.nodes():
                    if node not in self.visited:
                        stack.append(node)
                        order.append(node)
                        self.visited[node]=True
                        dfs()
                self.visited = {}
                print order
                return order

