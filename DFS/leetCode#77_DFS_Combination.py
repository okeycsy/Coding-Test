class Solution:
    def combine(self, n: int, k: int):
        ret = []

        def DFS(elements, start):
            #종료조건
            if len(elements) == k:
                ret.append(elements[:])
                return

            for i in range(start, n):
                elements.append(i+1)
                DFS(elements, i+1)
                elements.pop()

        DFS([],0)
        return ret

S = Solution()
print(S.combine(4,2))