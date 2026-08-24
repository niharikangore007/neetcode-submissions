class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_value = -1
        for i in range(len(arr) -1,-1,-1):
            temp = arr[i]
            arr[i] = max_value
            max_value = max(max_value , temp)
        return arr    
