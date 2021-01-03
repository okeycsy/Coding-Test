class Solution:
    def sol(self,s:str)->bool:
        stack = []
        #Mapping Table
        table = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for char in s:
            if char not in table:
                stack.append(char)
            elif table[char] !=stack.pop() or not stack:
                return False

        return True
