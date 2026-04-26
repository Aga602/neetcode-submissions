class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = {}
        y = {}
        for i in s:
            if i in x:
                x[i] = 1 + x[i]
            else:
                x[i] = 1
        
        for j in t:
            if j in y:
                y[j] = 1 + y[j]
            else:
                y[j] = 1
        
        print(x,y)

        if x == y:
            return True
        else:
            return False
