class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        smallest = float('inf')
        smallestIndex = 0
        while k:
            for i in range(len(nums)):
                if smallest > nums[i]:
                    smallest = nums[i]
                    smallestIndex = i
            nums[smallestIndex] = smallest * multiplier
            smallest = float('inf')
            k-=1
        return nums
