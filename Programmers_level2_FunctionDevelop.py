def solution(progresses:list, speeds:list)->list:
    stack = []
    isDone=[]
    count = 0
    answer = []

    for i in range(0, len(progresses)):
        stack.append(i)

    while stack:
        for i in range(0,len(progresses)):
            progresses[i]+=speeds[i]
            if progresses[i]>=100:
                isDone.append(i)
                isDone.sort()
                progresses[i], speeds[i]= 0,0

        while isDone and stack[0]==isDone[0]:
            count+=1
            stack.pop(0)
            isDone.pop(0)

        if count!=0:
            answer.append(count)
            count = 0

    return answer


ret = solution([99,99,99],[1,30,5])
print(ret)