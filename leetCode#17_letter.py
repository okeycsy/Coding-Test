class Solution:
    def Combination(self, digits:str):
        ret = []
        dic = {"2":"abc","3":"def","4":"ghi","5":"jkl",
               "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
        }
        #재귀 탐색을 위해 index(시작)과 path(경로)를 파라메터로 넘김
        def dfs(index, path):
            #종료조건
            if len(path)==len(digits):
                ret.append(path)
                return

            #반복조건
            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i+1,path+j)

        if not digits:
            return []

        dfs(0,"")
        return ret
