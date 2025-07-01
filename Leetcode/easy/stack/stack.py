class Solution:
    def isValid(self, s: str) -> bool:
        sign = {")":"(","}":"{","]":"["}
        stack = []
        if len(s) <= 1 and len(s)%2 != 0:
            return False
        for i in s:
            if i not in sign:
                stack.append(i)
            else:
                if len(stack) ==0:
                    return False
                if  stack.pop() != sign[i]:
                    return False
        return True if len(stack)==0 else False

        
        