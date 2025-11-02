from heapq import *


class Solution:
    def findClosestElements(self, arr, K, X):
        """ Leetcode 658 """
        min_heap = []
        result = []

        for num in arr:
            heappush(min_heap, (abs(num - X), num))

        while K != 0:
            result.append(heappop(min_heap)[1])
            K -= 1
        return sorted(result)
