class Solution:
    def Permutation(self,nums:list):
        results=[]
        prev_elements=[]

        def DFS(elements):
            if len(elements)==0:
                #Append with Copy One
                results.append(prev_elements[:])
                return

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                DFS(next_elements)
                #맨 오른쪽 원소부터 pop
                prev_elements.pop()

        DFS(nums)
        return results

s = Solution()
ans = s.Permutation([1,2,3])
print(ans)