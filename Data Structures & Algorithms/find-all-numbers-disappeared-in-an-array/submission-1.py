class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 1
        n = len(nums)
        res = []
        numsDict = {}
        for j in range(len(nums)):
            numsDict[nums[j]] = j
        while i<=n:
            if i not in numsDict:
                res.append(i)
            i+=1
        
        return res