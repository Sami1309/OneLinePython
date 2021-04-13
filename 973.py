# https://leetcode.com/problems/k-closest-points-to-origin/
import heapq


class Solution:
    def kClosest(self, points, k: int):
        return heapq.nsmallest(k, points, key=lambda point: point[0]**2 + point[1]**2)
