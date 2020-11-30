class Solution:
    def twoSum(self, nums, target):
        newdict = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp not in newdict:
                newdict[nums[i]] = i
            else:
                return [newdict[temp], i]