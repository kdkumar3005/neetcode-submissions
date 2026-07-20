class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dict1 ={}
        res = []
        remain = []
        for i in range(len(arr1)):
            dict1[arr1[i]] = dict1.get(arr1[i],0)+1
        for j in range(len(arr2)):
            res+= [arr2[j]]*dict1[arr2[j]]

        for k in range(len(arr1)):
            if arr1[k] not in arr2:
                remain.append(arr1[k])
        print(remain)
        print(dict1)
        remain = sorted(remain)
        
        
        return res + remain