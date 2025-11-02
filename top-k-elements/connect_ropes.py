from heapq import *


class Solution:
    def minimumCostToConnectRopes(self, ropeLengths):
        heap = []

        # push all the rope lengths to the min heap
        for length in ropeLengths:
            heappush(heap, length)

        total_cost = 0
        while len(heap) > 1:
            rope1 = heappop(heap)
            rope2 = heappop(heap)

            cost = rope1 + rope2
            total_cost += cost
            heappush(heap, cost)

        return total_cost


def main():
    sol = Solution()
    print("Minimum cost to connect ropes: " +
          str(sol.minimumCostToConnectRopes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
          str(sol.minimumCostToConnectRopes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
          str(sol.minimumCostToConnectRopes([1, 3, 11, 5, 2])))


main()
