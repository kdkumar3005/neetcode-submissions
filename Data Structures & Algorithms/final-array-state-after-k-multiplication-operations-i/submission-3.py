class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(value,index) for index,value in enumerate(nums)]
        heapq.heapify(heap)
        while k:
            num,idx = heapq.heappop(heap)
            print(num,idx)
            heapq.heappush(heap,(num*multiplier,idx))
            nums[idx] = num*multiplier
            k-=1
            
        return nums