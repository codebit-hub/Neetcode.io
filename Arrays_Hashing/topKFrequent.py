"""
Top K Frequent Elements
Given an integer array nums and an integer k,
return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

Example 2:

Input: nums = [7,7], k = 1

Output: [7]

Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # number of frequences can't be negative or
        # not higher than length of nums
        if k < 0 or k > len(nums):
            k = len(nums) - 1

        # create empty dict for processing nums
        count: dict[int, int] = {}

        # add all numbers from nums into dict
        # hashing eliminates doubles
        # this creates num: frequency dict
        for num in nums:
            count[num] = count.get(num, 0) + 1
        print(f"count dict: {count.items()}")

        # create list of empty buckets (lists) for each num
        freq: list[list[int]] = [[] for _ in range(len(nums) + 1)]

        # Volume of counts can't exceed length of nums
        # Counts will be always <= length of nums
        # There will be always enougp buckets in freq
        for num, counts in count.items():
            freq[counts].append(num)
        print(f"freq: {freq}")

        res: list[int] = []
        for i in range(len(nums), 0, -1):
            # Sorted listing of top frequencies
            # for num in sorted(freq[i], reverse=True):
            # Unsorted listing of top frequencies
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res


if __name__ == "__main__":
    nums1: list[int] = [1, 2, 2, 2, 4, 4, 3, 3, 5, 5, 7, 7, 7]
    k1: int = 3

    nums2: list[int] = [7, 7]
    k2: int = 1

    print(f"Output1: {Solution().topKFrequent(nums1, k1)}")
    print(f"Output2: {Solution().topKFrequent(nums2, k2)}")
