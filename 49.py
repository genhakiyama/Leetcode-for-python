from collections import Counter
from collections import defaultdict

class Solution :
    def groupAnagrams(self , strs : list[str]) -> list[list[str]] :
        result = []
        d = defaultdict(list)

        for x in strs :
            d["".join(sorted(x))].append(x)

        return list(d.values())

data = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(data))