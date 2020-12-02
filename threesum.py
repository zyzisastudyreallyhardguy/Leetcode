#best solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N, result = len(nums), []
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * -1
            s, e = i + 1, N - 1
            while s < e:
                sum_result = nums[s] + nums[e]
                if sum_result == target:
                    result.append([nums[i], nums[s], nums[e]])
                    s = s + 1
                    while s < e and nums[s] == nums[s - 1]:
                        s = s + 1
                elif sum_result < target:
                    s = s + 1
                else:
                    e = e - 1
        return result

#mysolution
class Solution:
    def threeSum(nums):
        allcombination = []
        newdict = {}
        result = []
        nums.sort()
        # initialize newdict o(n)
        for element in nums:
            newdict[element] = []

        for i in range(len(nums)):  # find all pairs for allcombination
            for j in range(i + 1, len(nums)):
                allcombination.append([i, j])

        for i, element in enumerate(nums):  # o(n)
            newdict[element].append(i)

        for element in allcombination:
            residual = 0 - sum([nums[element[0]], nums[element[1]]])
            print(residual)
            if residual in newdict:
                for thing in newdict[residual]:
                    if thing not in element and thing > element[1]:
                        temp = [nums[element[0]], nums[element[1]], nums[thing]]
                        if temp not in result:
                            result.append(temp)
        return result
