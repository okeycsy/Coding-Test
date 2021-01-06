class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #for Hash Table
        table={}
        #string Concat에서 list형 자료구조를 쓰는 습관을 들이자
        longestOne=0

        for i in range(len(s)):
            localLongest=0
            table[s[i]]=1
            localLongest+=1
            longestOne=max(longestOne,localLongest)

            for j in range(i+1,len(s)):
                if s[j] not in table:
                    localLongest+=1
                    table[s[j]]=1
                    longestOne=max(longestOne,localLongest)

                else:
                    table.clear()
                    longestOne=max(longestOne,localLongest)

                    break

        return longestOne
​