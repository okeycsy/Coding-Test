import collections

def solution(clothes):
    answer=1
    collect = collections.defaultdict(int)

    for row in clothes:
        collect[row[1]]+=1

    for val in collect.values():
        answer*=(val+1)

    return answer-1