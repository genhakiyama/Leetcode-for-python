import math 

class Solution :
    def merge(self , intervals : list[list[int]]) -> list[list[int]] :
        intervals.sort(key = lambda x : x[0])
        merges = []

        for segment in intervals :
            if not merges or merges[-1][1] < segment[0] :
                merges.append(segment)
            else :
                merges[-1][1] = max(merges[-1][1] , segment[1])
        
        return merges

arr = [[15,18] , [1,3],[2,6],[8,10]]
print(Solution().merge(arr))