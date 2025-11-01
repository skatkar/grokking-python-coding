from heapq import heappop, heappush


class Solution:
    def findKthSmallestNumber(self, nums, k):
        """Find the k-th smallest number in an array."""
        minHeapq = []
        for num in nums:
            heappush(minHeapq, num)

        i = 1
        while i < k:
            heappop(minHeapq)
            i += 1
        return heappop(minHeapq)


def main():
    sol = Solution()
    nums = [7, 10, 4, 3, 20, 15]
    k = 3
    print(
        f"The {k}-th smallest number in {nums} is: {sol.findKthSmallestNumber(nums, k)}")


main()
