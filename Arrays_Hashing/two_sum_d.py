"""
Given an array of integers nums and an integer target,
return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j
that satisfy the condition.

Return the answer with the smaller index first.
Example 1:

Input:
nums = [3,4,5,6], target = 7

Output: [0,1]
"""

from typing import List


"""
Solution1: 
    Time: O(n^2)
    Space: O(1)
"""

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


solution1 = Solution1()
nums1 = [3, 4, 5, 6]
nums2 = [4, 5, 6]
nums3 = [5, 5]
target1 = 7
target2 = 10
target3 = 10
print(f"Output1: {solution1.twoSum(nums=nums1, target=target1)}")
print(f"Output2: {solution1.twoSum(nums=nums2, target=target2)}")
print(f"Output3: {solution1.twoSum(nums=nums3, target=target3)}")


"""
Solution2:
    Time: O(1)
    Space: O(1)
"""

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, nu in enumerate(nums):
            complement = target - nu
            if complement in seen:
                return [seen[complement], i]
            seen[nu] = i

solution2 = Solution2()
nums4 = [3, 4, 5, 6]
nums5 = [4, 5, 6]
nums6 = [5, 5]
target4 = 7
target5 = 10
target6 = 10
print(f"Output4: {solution2.twoSum(nums=nums4, target=target4)}")
print(f"Output5: {solution2.twoSum(nums=nums5, target=target5)}")
print(f"Output6: {solution2.twoSum(nums=nums6, target=target6)}")
