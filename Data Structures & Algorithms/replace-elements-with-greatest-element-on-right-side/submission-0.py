class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(0,len(arr)-1):
            if i+1 != len(arr):
                arr[i] = sorted(arr[i+1:])[-1]
        arr[-1]  = -1   
        return arr