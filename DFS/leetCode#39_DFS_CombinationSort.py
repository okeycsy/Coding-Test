class Solution:
    def combinationSum(self, candidates: list, target: int):
        ret = []

        def DFS(element,sum, start):
            if sum==target:
                ret.append(element[:])
                return

            elif sum>target:
                return

            #재귀조건
            for i in range(start, len(candidates)):
                element.append(candidates[i])
                DFS(element, sum+candidates[i],i)
                #맨 오른쪽부터 pop
                element.pop()

        DFS([],0,0)
        return ret

S = Solution()
print(S.combinationSum([2,3,5],8))