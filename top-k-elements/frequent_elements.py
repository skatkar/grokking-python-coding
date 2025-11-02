from heapq import *


class Solution:
    def findTopKFrequentNumbers(self, nums, k):
        frequency_map = {}
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1

        minHeap = []
        for num, frequency in frequency_map.items():
            heappush(minHeap, (frequency, num))
            if len(minHeap) > k:
                heappop(minHeap)

        top_k_numbers = []
        while minHeap:
            top_k_numbers.append(heappop(minHeap)[1])

        return top_k_numbers
