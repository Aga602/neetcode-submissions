class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = []
        for i in nums:
            if i == 1:
                count = count + 1
            else:
                max_count.append(count)
                count = 0
        max_count.append(count)
        return (sorted(max_count, reverse=True)[0])