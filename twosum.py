#solution 1 brute force
class Solution1:
    def twoSum(self, nums, target):
        newlist = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]



#solution 2 dictionary based solution
#version 1
class Solution2:
    def twoSum(self, nums, target):
        newdict = {}
        for i,element in enumerate(nums):
            newdict[element] = i
        for i,element in enumerate(nums):
            if (target - element) in newdict:
                return [i,newdict[target - element]]

#version 2
class Solution2:
    def twoSum(self, nums, target):
        newdict = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp not in newdict:
                newdict[nums[i]] = i
            else:
                return [newdict[temp], i]
