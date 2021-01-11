import itertools

def combination(n:int, k:int):
    nums =[]
    for i in range(n):
        nums.append(i+1)
    return list(map(list,itertools.combinations(nums,k)))

ans = combination(4,2)
print(ans)