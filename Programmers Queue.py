def solution(bridge_length, weight, truck_weights):
    #First in First out
    q = [0]*bridge_length
    sec = 0

    while q:
        sec+=1
        q.pop(0)
        if truck_weights:
            if (sum(q)+truck_weights[0])<=weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return sec

print(solution(2,10,[7,4,5,6]))