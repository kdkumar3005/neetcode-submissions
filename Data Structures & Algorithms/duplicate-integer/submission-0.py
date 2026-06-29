class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = defaultdict(int)
        for i in nums:
            if nums_dict[i] == 0:
                nums_dict[i]+=1
            else:
                return True
        return False