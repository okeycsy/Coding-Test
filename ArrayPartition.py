class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pair=[]
        sums=0

        for i in nums:
            pair.append(i)
            if len(pair)==2:
                sums+=min(pair)
                #init
                pair=[]

        return sums