from typing import List

nums = [2, 7, 11, 15]
nums2 = [3, 2, 4]
nums3 = [3, 3]
nums4 = [3, 2, 3]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            if sum(nums) == target:
                return [0, 1]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]




sol = Solution()

print(sol.twoSum(nums, 9))
print(sol.twoSum(nums2, 6))
print(sol.twoSum(nums3, 6))
print(sol.twoSum(nums4, 6))