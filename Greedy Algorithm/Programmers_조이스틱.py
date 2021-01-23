def solution(name):
    answer=0
    name=list(name)

    n=len(name)
    #A = 65, Z = 90
    for idx, val in enumerate(name):
        diff = ord(val)-ord('A')
        if diff>12:
            diff=26-diff

        answer+=diff

    idx=0
    left_idx=0
    right_idx=0
    name[idx]='A'
    while True:
        left_cnt=0
        right_cnt=0
        for i in range(n):
            right_cnt += 1
            right_idx += 1
            if right_idx > 0:
                right_idx -= n
            if name[right_idx] != 'A':
                name[right_idx] = 'A'
                break

            left_cnt+=1
            left_idx-=1

            if left_idx<0:
                left_idx+=n
            if name[left_idx]!='A':
                name[left_idx]='A'
                break

        answer+=max(left_cnt,right_cnt)
        if left_cnt<right_cnt:
            idx+=right_cnt
            if idx>0:
                idx-=n
        else:
            idx-=left_cnt
            if idx<0:
                idx+=n

        left_idx=idx; right_idx=idx

        #종료조건
        isBreak=True
        for char in name:
            if 'A' !=char:
                isBreak=False
                break

        if isBreak:
            break
    return answer


print(solution('JEROEN'))

'''
a=['A','A','A']
isbreak=True
for char in a:
    if char != 'A':
        isbreak=False

print(isbreak)
'''