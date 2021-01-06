import collections

def solution(participant:list, completionlist)->str:
    part = collections.Counter(participant)

    for comp in completionlist:
        if comp in part:
            part[comp]-=1

    part_sort = sorted(part.items(),key=lambda x:x[1],reverse=True)
    return part_sort[0][0]
​