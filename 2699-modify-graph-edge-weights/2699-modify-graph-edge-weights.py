# :type n: int
# :type edges: List[List[int]]
# :type source: int
# :type destination: int
# :type target: int
# :rtype: List[List[int]]

import heapq

class Solution(object):
    def modifiedGraphEdges(self, n, edges, source, destination, target):
        # Create an adjacency list representation of the graph
        adjs = [{} for _ in range(n)]
        for edge in edges:
            adjs[edge[0]][edge[1]] = edge[2]
            adjs[edge[1]][edge[0]] = edge[2]

        # Initialize an array to store the minimum distance to each node, initially set to infinity
        distTo = [float('inf')] * n
        distTo[source] = 0

        # Initialize a priority queue (min-heap) with the source node and its distance
        pq = [(0, source)]
        heapq.heapify(pq)

        # Apply Dijkstra's algorithm to find the shortest path from the source
        self.dijkstra(adjs, distTo, pq)

        # Check if the shortest path to the destination node is equal to the target distance
        if distTo[destination] == target:
            # If equal, return the edges (replace -1 with some large value)
            return self.fill(edges)
        elif distTo[destination] < target:
            # If the shortest path is shorter than the target, no valid path exists
            return []

        # If the shortest path exceeds the target distance, modify the graph to reduce it
        for edge in edges:
            if edge[2] == -1:
                # Replace the weight of the -1 edge with 1
                edge[2] = 1
                adjs[edge[0]][edge[1]] = 1
                adjs[edge[1]][edge[0]] = 1

                # Create a priority queue with the nodes affected by the modified edge
                pq = [(distTo[edge[0]], edge[0]), (distTo[edge[1]], edge[1])]

                # Recalculate distances using Dijkstra's algorithm
                self.dijkstra(adjs, distTo, pq)

                # Check if the modified graph now has a valid path
                if distTo[destination] == target:
                    # If equal, return the edges
                    return self.fill(edges)
                elif distTo[destination] < target:
                    # Adjust the weight of the modified edge to meet the target distance
                    edge[2] += target - distTo[destination]
                    adjs[edge[0]][edge[1]] = edge[2]
                    adjs[edge[1]][edge[0]] = edge[2]
                    return self.fill(edges)

        # If no valid path can be found, return an empty list
        return []

    def fill(self, edges):
        # Replace placeholder weights (-1) with a large value.
        for edge in edges:
            if edge[2] == -1:
                edge[2] = int(2e9)
        return edges

    def dijkstra(self, adjs, distTo, pq):
        # Dijkstra's algorithm for finding the shortest path.
        while pq:
            curr_dist, curr = heapq.heappop(pq)

            for next_node, weight in adjs[curr].items():
                if weight > 0:
                    if distTo[next_node] > distTo[curr] + weight:
                        distTo[next_node] = distTo[curr] + weight
                        heapq.heappush(pq, (distTo[next_node], next_node))
