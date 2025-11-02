from heapq import *


class Solution:

    def __init__(self, nums, k):
        self.min_heap = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, num):
        heappush(self.min_heap, num)

        if len(self.min_heap) > self.k:
            heappop(self.min_heap)
        return self.min_heap[0]
