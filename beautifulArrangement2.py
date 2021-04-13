# https://leetcode.com/problems/beautiful-arrangement-ii/

class Solution:
    def constructArray(self, n: int, k: int):
        return [(3*n-k-i+1)//2 if (i + k - n >= 0 and (i + k - n) % 2 == 1) else i - (max(0, (i + k - n)//2)) for i in range(1, n+1)]
