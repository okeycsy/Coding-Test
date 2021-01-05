class Solution():
    def sol(self, J:str, S:str)->int:
        table = {}
        count = 0

        for char in S:
            if char not in table:
                table[char]=1
            elif char in table:
                table[char]+=1

        for char in J:
            if char in table:
                count+=table[char]

        return count