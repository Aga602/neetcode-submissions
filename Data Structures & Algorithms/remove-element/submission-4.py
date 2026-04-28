class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(0,len(nums)):
            if nums[i] == val:
                for j in range(i+1, len(nums)):
                    if nums[j] != val:
                        nums[i], nums[j] = nums[j], nums[i]
        
        if val in nums:
            return nums.index(val)
        else:
            return len(nums)


            