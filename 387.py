from collections import Counter
import string 

class Solution :
    def firstUniqChar(self , s : str) -> int :
        appeared = dict()
        # we also can use appeared = Counter(s) instead

        for x in s :
            appeared[x] = appeared.get(x , 0) + 1

        for index , x in enumerate(s , 0) :
            if appeared[x] == 1 :
                return index 

        return -1

s = input()
print(Solution().firstUniqChar(s))
