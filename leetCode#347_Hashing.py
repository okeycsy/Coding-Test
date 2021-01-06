class Solution():
    def sol(self, nums:list, k:int)->list:
        table = {}
        ret = []

        #Make a Hash Table
        for num in nums:
            if num not in table:
                table[num]=1
            else:
                table[num]+=1

        table_sort = sorted(table.items(), key = lambda x:x[0])
        print(table_sort)
        #print(table_sort)
        for i in range(2):
            ret.append(table_sort[i][0])

        return ret

S = Solution()
print(S.sol([1,1,1,2,2,3],2))
