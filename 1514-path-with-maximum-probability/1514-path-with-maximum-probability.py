import heapq
from collections import defaultdict

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        # Build the graph
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            prob = succProb[i]
            graph[u].append((v, prob))
            graph[v].append((u, prob))
        
        # Max-heap priority queue: store (negative prob, node)
        max_heap = [(-1, start_node)]
        
        # Dictionary to store the maximum probability to reach each node
        max_prob = {i: 0 for i in range(n)}
        max_prob[start_node] = 1
        
        while max_heap:
            curr_prob, node = heapq.heappop(max_heap)
            curr_prob = -curr_prob  # Convert back to positive
            
            # If we've reached the end node, return the probability
            if node == end_node:
                return curr_prob
            
            # Explore neighbors
            for neighbor, prob in graph[node]:
                new_prob = curr_prob * prob
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))
        
        return 0.0

# Example usage:
# solution = Solution()
# n = 3
# edges = [[0, 1], [1, 2], [0, 2]]
# succProb = [0.5, 0.5, 0.2]
# start_node = 0
# end_node = 2
# print(solution.maxProbability(n, edges, succProb, start_node, end_node))  # Output: 0.25000
