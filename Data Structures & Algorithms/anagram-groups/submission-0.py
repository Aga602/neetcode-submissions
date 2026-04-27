class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []

        for i in range(0,len(strs)):        
            if strs[i] not in [sub for y in groups for sub in y ]:   
                first = {}
                inner_group = [strs[i]]
                for letter in strs[i]:
                    if letter in first:
                        first[letter] = first[letter] + 1
                    else:
                        first[letter] = 1
                for j in range(i+1, len(strs)):
                    second = {}
                    for letter in strs[j]:
                        if letter in second:
                            second[letter] = second[letter] + 1
                        else:
                            second[letter] = 1
                    
                    if second == first:
                        inner_group.append(strs[j]) 
                groups.append(inner_group)

        return groups



