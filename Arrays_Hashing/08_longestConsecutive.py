"""
Longest Consecutive Sequence
Medium

Given an array of integers nums, return the length of
the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements
in which each element is exactly 1 greater than the previous element.
The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 100,000
-10^9 <= nums[i] <= 10^9
"""


class Solution1:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        unique_nums = sorted(set(nums))
        best = 1
        current = 1

        for i in range(1, len(unique_nums)):
            if unique_nums[i] == unique_nums[i - 1] + 1:
                current += 1
            else:
                best = max(best, current)
                current = 1
        return max(best, current)


class Solution2:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            # skip non-starts
            if num - 1 in nums_set:
                continue

            steps = 1
            while num + steps in nums_set:
                steps += 1
            longest = max(longest, steps)

        return longest


nums1 = [2, 20, 4, 5, 7, 8, 9, 10, 3, 4, 5]
print(f"Output nums1: {Solution1().longestConsecutive(nums1)}")

nums2 = [2, 20, 4, 5, 7, 8, 9, 10, 3, 4, 5]
print(f"Output nums2: {Solution2().longestConsecutive(nums2)}")
