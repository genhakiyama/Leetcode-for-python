class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        my_dict = {')' : '(' , ']' : '[' , '}' : '{'}

        for c in s :
            if c in my_dict :
                top_element = stack.pop() if stack else '#'
                if (top_element != my_dict[c]) :
                    return False 
            else :
                stack.append(c)

        return False if stack else True

s = input()
print(Solution().isValid(s))