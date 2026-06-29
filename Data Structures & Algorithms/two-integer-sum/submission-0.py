class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_dict = defaultdict(int)
        res = []
        for i,val in enumerate(nums):
            if(target-val in list_dict):
                return[list_dict[target-val],i]
            list_dict[val] = i