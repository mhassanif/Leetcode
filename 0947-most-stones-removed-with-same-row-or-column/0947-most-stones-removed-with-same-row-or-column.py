class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))
                self.rank = [1] * size

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])  # Path compression
                return self.parent[x]

            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)
                
                if rootX != rootY:
                    # Union by rank
                    if self.rank[rootX] > self.rank[rootY]:
                        self.parent[rootY] = rootX
                    elif self.rank[rootX] < self.rank[rootY]:
                        self.parent[rootX] = rootY
                    else:
                        self.parent[rootY] = rootX
                        self.rank[rootX] += 1

        n = len(stones)
        uf = UnionFind(n)
        
        row_map = {}
        col_map = {}
        
        for i, (x, y) in enumerate(stones):
            if x not in row_map:
                row_map[x] = i
            else:
                uf.union(row_map[x], i)
            
            if y not in col_map:
                col_map[y] = i
            else:
                uf.union(col_map[y], i)
        
        # Find the number of unique components
        unique_components = len(set(uf.find(i) for i in range(n)))
        
        # Maximum number of stones that can be removed is total stones minus number of components
        return n - unique_components
