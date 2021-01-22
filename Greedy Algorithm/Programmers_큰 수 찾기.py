def solution(number,k):
    stack=[]
    n=len(number)
    answer=''

    for i in range(n):
        if not stack:
            stack.append(number[i])
            continue

        Finish = False

        #stack의 top과 비교
        while stack and stack[-1]<number[i]:
            stack.pop()
            k-=1
            if not k:
                Finish=True
                break

        stack.append(number[i])

        if Finish:
            stack+=number[i+1:]
            break

    if len(stack)==n:
        answer=''.join(stack[:k])
    else:
        answer=''.join(stack)

    return answer
solution('4177252841',4)

