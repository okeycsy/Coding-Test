import collections


def solution(clothes):
    answer = 1
    equipment = []

    for row in clothes:
        equipment.append(row[1])

    collect = collections.Counter(equipment)
    for val in collect.values():
        answer *= (val + 1)

    return answer - 1