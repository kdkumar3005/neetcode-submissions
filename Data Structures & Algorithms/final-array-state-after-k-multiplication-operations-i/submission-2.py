class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(value,index) for index,value in enumerate(nums)]
        heapq.heapify(heap)
        while k:
            num,idx = heapq.heappop(heap)
            print(num,idx)
            heapq.heappush(heap,(num*multiplier,idx))
            k-=1
        for i in range(len(heap)):
            num,idx = heapq.heappop(heap)
            nums[idx] = num
        return nums