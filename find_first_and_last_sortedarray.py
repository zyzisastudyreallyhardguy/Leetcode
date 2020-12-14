class Solution:
    def binarysearch(self, nums, target):
        start = 0
        end = len(nums)
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        return start

    def searchRange(self, nums, target: int):
        if len(nums):
            if (nums[0] > target) or (target > nums[len(nums) - 1]):
                return [-1, -1]
            start = self.binarysearch(nums, target)
            if nums[start] != target:
                return [-1, -1]
            return [start, self.binarysearch(nums, target + 1) - 1]
        else:
            return [-1, -1]
