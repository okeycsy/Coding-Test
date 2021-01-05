import random
TRIAL = 100000

#23명일때 생일 문제의 확률
def samebirthProblem():
    same_birth = 0

    #100000번 시도
    for _ in range(TRIAL):
        births = []
        for i in range(50):
            birth = random.randint(1,365)
            if birth in births:
                same_birth+=1
                break
            births.append(birth)

    return same_birth

print(f'{samebirthProblem()/TRIAL*100}%')