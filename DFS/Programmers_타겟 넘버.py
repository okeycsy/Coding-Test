def solution(numbers, target):
    answer = 0
    def DFS(index, sum):
        # 종료조건 -> 깊이가 5인 케이스
        if index == len(numbers):
            if sum == target:
                nonlocal answer
                answer+=1
            return

        #for문을 쓸 필요가 없다. 왜냐하면 우리는 자식 노드가 2개인 재귀 호출을 원하므로
        DFS(index+1, sum+numbers[index])
        DFS(index+1, sum-numbers[index])

    DFS(0,0)
    return answer

print(solution([1,1,1,1,1],3))