class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i in nums:
            if i in frequency:
                frequency[i] = frequency[i] + 1
            else:
                frequency[i] = 1
        
        sorted_dict = dict(sorted(frequency.items(), key=lambda item: item[1], reverse = True))
        
        x = []
        for key, _ in sorted_dict.items():
            x.append(key)

        return x[:k]