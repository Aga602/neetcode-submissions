class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        matches = {}
        for i in nums:
            matches[i] = 0
        for i in nums:
            matches[i] = matches[i] + 1
        duplications = False
        for _, values in matches.items():
            if values > 1:
                duplications = True
        return duplications
