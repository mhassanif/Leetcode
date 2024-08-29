#    :type stones: List[List[int]]
#    :rtype: int

class Solution(object):
    def removeStones(self, stones):

        # defaultdict adds a node if not found --> no error
        from collections import defaultdict

        #dfs traversal makring vsisited row then cols vise
        def dfs(x, y):
            visited.add((x, y))
            for ny in rows[x]:
                if (x, ny) not in visited:
                    dfs(x, ny)
            for nx in cols[y]:
                if (nx, y) not in visited:
                    dfs(nx, y)

        #initiallize dictionaries
        rows = defaultdict(list)
        cols = defaultdict(list)
        
        # setting up the adjacency lists
        for x, y in stones:
            rows[x].append(y)
            cols[y].append(x)
        
        # keep track of already explored stones
        visited = set()

        #counter for seprate components
        components = 0
        
        # perform dfs if not aleady visited --> ie new componenet found
        for x, y in stones:
            if (x, y) not in visited:
                dfs(x, y)
                components += 1

        return len(stones) - components

# represent stones as graph nodes with edges
# builds adjacency lists for stones
# use DFS to identify/count inter-connected components
# each component can only leave one stone behind
#  ie number of remaining stones is equal to components
# removable stones = total - number of connected components 
