import ast 

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        data = dict()

        for x in nums :
            data[x] = data.get(x , 0) + 1

        data = dict(sorted(data.items() , reverse = True))
        tot = 0
        for x,y in data.items() :
            tot += y
            if tot >= k :
                return x 
            

raw_input = input()
arr = ast.literal_eval(raw_input)
k = int(input())
print(Solution().findKthLargest(arr , k))