"""
Products of Array Except Self
Medium
Topics
Company Tags
Hints
Given an integer array nums, return an array output where output[i] is
the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in
O
(
n
)
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 100,000
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed
to fit in a 32-bit integer.
"""

class Solution1:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        prefix_lst = []
        postfix_lst = []
        result_lst = []

        prefix = 1
        for num in nums:
            prefix_lst.append(prefix * num)
            prefix *= num

        postfix = 1
        postfix_lst = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            postfix_lst[i] = postfix * nums[i]
            postfix *= nums[i]

        for i in range(len(nums)):
            left = prefix_lst[i - 1] if i > 0 else 1
            right = postfix_lst[i + 1] if i < len(nums) - 1 else 1
            result_lst.append(left * right)

        return result_lst


nums1 = [1,2,3,4]
output1 = Solution1().productExceptSelf(nums1)
print(f"output1: {output1}")
