class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1

        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid

        left = start
        start = 0
        end = len(nums) - 1
        if (target >= nums[left]) and (target <= nums[end]):
            start = left
        else:
            end = left

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return -1

