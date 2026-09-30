"""Given two strings s and t, return true if the two strings are anagrams
of each other, otherwise return false.

Two strings are anagrams if they contain the same characters,
with each character appearing the same number of times, regardless of order.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False
