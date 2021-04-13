# https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        return words == sorted(words, key=lambda w: [order.index(let) for let in w])
