class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        mid = 0

        while start <= end:
            mid = (start+end) // 2

            # if TARGET is greater, ignore left half
            if nums[mid] < target:
                # new start (aka "low") is at mid pos.+1
                start = mid+1
            
            # if TARGET is smaller, ignore right half
            elif nums[mid] > target:
                # new end (aka "high") is at mid pos.-1
                end = mid-1
            
            # otherwise the target is found
            else:
                return mid
    
         # if target does not exist
        return -1