# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s = "".join(sorted(s))
#         t = "".join(sorted(t))

#         return t == s

# s = input()
# t = input()
# print(Solution().isAnagram(s , t))

from collections import Counter

class Solution :
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)