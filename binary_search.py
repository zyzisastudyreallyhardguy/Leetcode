class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        notarget = True
        while left <= right:
            midpoint = left + (right - left) // 2
            if nums[midpoint] == target:
                notarget = False
                return midpoint
            elif nums[midpoint] > target:
                right = midpoint - 1
            else:
                left = midpoint + 1
        if notarget == True:
            return -1