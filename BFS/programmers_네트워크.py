def solution(n, computers):
    #solved by BFS
    answer = 0
    bfs_queue = []
    visited = [0]*n

    while 0 in visited:
        x=visited.index(0)
        bfs_queue.append(x)
        visited[x]=1

        while bfs_queue:
            node = bfs_queue.pop(0)

            for i in range(n):
                if visited[i]==0 and computers[node][i]==1:
                    bfs_queue.append(i)
                    visited[i]=1
        answer+=1
    return answer



print(solution(3,[[1,1,0],[1,1,0],[0,0,1]]))