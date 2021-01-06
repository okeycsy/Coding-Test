def solution(phone_book:list):
    phone_book.sort()
    isIn=False

    for i in range(len(phone_book)):
        for j in range(i+1,len(phone_book)):
            if phone_book[j].find(phone_book[i],0,len(phone_book[i]))!=-1:
                isIn=True
        if isIn:
            break

    return not isIn