class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2Dict = {}
        res = []

        for i in range(len(nums2)):
            nums2Dict[nums2[i]] = i

        for num in nums1:
            index = nums2Dict[num]
            found = False
            for j in range(index+1, len(nums2)):
                if nums2[j] > num:
                    res.append(nums2[j])
                    found = True
                    break
            if not found:
                res.append(-1)
        
        return res