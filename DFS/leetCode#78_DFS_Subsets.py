class Solution:
    def subset(self,nums:list):
        ret = []

        def DFS(index, path):
            ret.append(path)

            for i in range(index, len(nums)):
                DFS(i+1,path+[nums[i]])

        DFS(0,[])
        return ret

S = Solution()
print(S.subset([1,2,3]))