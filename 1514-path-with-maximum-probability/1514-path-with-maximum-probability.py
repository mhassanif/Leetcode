#  :type n: int
#  :type edges: List[List[int]]
#  :type succProb: List[float]
#  :type start_node: int
#  :type end_node: int
#  :rtype: float

import heapq
from collections import defaultdict

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):

        # Build the graph adjacency list
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            prob = succProb[i]
            graph[u].append((v, prob))
            graph[v].append((u, prob))
        
        # Max-heap priority queue: store (negative prob, node)
        max_heap = [(-1, start_node)]
        
        # maximum prob to reach each node from start node
        max_prob = {i: 0 for i in range(n)}
        max_prob[start_node] = 1
        
        while max_heap:
            curr_prob, node = heapq.heappop(max_heap)
            # Convert back to positive 
            curr_prob = -curr_prob  
            
            # If we've reached the end node, return the probability
            if node == end_node:
                return curr_prob
            
            # Explore neighbors
            for neighbor, prob in graph[node]:
                new_prob = curr_prob * prob

                if new_prob > max_prob[neighbor]:
                    # higher probability path to a node is found
                    max_prob[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))
        
        return 0.0

# heapq implements a min-heap by default ie pops the smallest element first
# To simulate max-heap --> store probabilities as negative in heap
# so "largest" ie most negative corresponds to highest probability.

# Modified Dijkstra’s Algorithm:

# Step 1: The algorithm begins by popping the node with the highest probability from the priority queue.

# Step 2: If this node is the end node, the algorithm stops, and we return the probability associated with it as this is the maximum probability path.

# Step 3: If it’s not the end node, we explore all its neighbors. For each neighbor:
# Calculate the probability of reaching the neighbor through the current path.
# If this probability is higher than any previously known probability to reach that neighbor, we update the neighbor’s probability and push it into the priority queue to explore it further.

# Step 4: Repeat the process until either the end node is reached or the priority queue is empty (meaning there’s no path to the end node).
