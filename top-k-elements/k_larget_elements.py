from heapq import heappop, heappush


class Solution:
    def findKLargestNumbers(self, nums, k):
        """Find the k largest numbers in an array."""
        minHeapq = []
        i = 0
        while i < k:
            heappush(minHeapq, nums[i])
            i += 1

        while i < len(nums):
            if nums[i] > minHeapq[0]:
                heappop(minHeapq)
                heappush(minHeapq, nums[i])
            i += 1
        return minHeapq


def main():
    sol = Solution()
    nums = [3, 1, 5, 12, 2, 11]
    k = 3
    print(
        f"The {k} largest numbers in {nums} are: {sol.findKLargestNumbers(nums, k)}")


main()
