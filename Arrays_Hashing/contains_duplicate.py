from typing import List, Set


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_nums: int = len(nums)
        set_nu: set = set(nums)
        len_nu: int = len(set_nu)
        if len_nums != len_nu:
            return True
        else:
            return False

duplicate = Solution()
input1 = [1, 2, 3, 3]
input2 = [1, 2, 3, 4]
print(f"Contains duplicate: {duplicate.hasDuplicate(nums=input1)}")
print(f"Contains duplicate: {duplicate.hasDuplicate(nums=input2)}")

"""
Time complexity O(n), Space: O(n)
"""
class Solution2:
    def hasDuplicate2(self, nums: List[int]) -> bool:
        set_nu: set = set()

        for n in nums:
            if n in set_nu:
                return True
            set_nu.add(n)
        return False


duplicate2 = Solution2()
input1 = [1, 2, 3, 3]
input2 = [1, 2, 3, 4]
print(f"Contains duplicate2: {duplicate2.hasDuplicate2(nums=input1)}")
print(f"Contains duplicate2: {duplicate2.hasDuplicate2(nums=input2)}")
