"""
Group Anagrams
Easy

Given an array of strings strs, group all anagrams together
into sublists.
You may return the output in any order.

An anagram is a string that contains the exact same characters
as another string,
but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 10000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
"""

# defaultdict changes the behaviour at runtime
from collections import defaultdict

# DefaultDirct needs only for type checking
from typing import DefaultDict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        # default dict provides a default value when a key is missing.
        result: DefaultDict[tuple[int, ...], list[str]] = defaultdict(list)

        for word in strs:
            count: list = [0] * 26
            for c in word:
                count[(ord(c) - ord("a"))] += 1
            key = tuple(count)
            result[key].append(word)
            # normal dict: result.setdefault(key, []).append(word)
            # or if key in result: result[key].append(word)
            #       else result[key] = word
            # hashable keys are only: int, float, str, tuple, frozenset
            # unhashable keys: list, dict, set, bytearray

        return list(result.values())


if __name__ == "__main__":
    # Input:
    strings1: list[str] = ["act", "pots", "tops", "cat", "stop", "hat"]
    strings2: list[str] = ["x"]
    strings3: list[str] = [""]
    # print(f"{strs}")
    print(f"Grouped anagrams: {Solution().groupAnagrams(strings1)}.")
    print(f"Grouped anagrams: {Solution().groupAnagrams(strings2)}.")
    print(f"Grouped anagrams: {Solution().groupAnagrams(strings3)}.")
