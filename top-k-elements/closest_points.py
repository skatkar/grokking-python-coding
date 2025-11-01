from heapq import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return (self.x ** 2 + self.y ** 2) < (other.x ** 2 + other.y ** 2)


class Solution:
    def findClosestPoints(self, points, k):
        heap = []
        for point in points:
            heappush(heap, point)

        result = [heappop(heap) for _ in range(min(k, len(heap)))]

        return result


def main():
    sol = Solution()
    points = [Point(1, 3), Point(3, 4), Point(2, -1)]
    k = 2
    closest_points = sol.findClosestPoints(points, k)
    print(f"The {k} closest points are:")
    for point in closest_points:
        print(f"({point.x}, {point.y})")


main()
