import collections

def solution(genres,plays):
    answer=[]
    Mapping={}

    #For Hash map
    for i in range(len(genres)):
        if genres[i] not in Mapping:
            Mapping[genres[i]]=plays[i]
        else:
            Mapping[genres[i]]+=plays[i]
    print(Mapping)

    #Sort by Value --> .items() 꼭 붙히기
    sort_Mapping = sorted(Mapping.items(), key=lambda x:x[1], reverse=True)
    genre_list=[]
    print(sort_Mapping)
    for i in range(len(sort_Mapping)):
        genre_list.append(sort_Mapping[i][0])
    print(genre_list)

    #Make a list (Sorting by Genre)
    for genre in genre_list:
        tmp = collections.defaultdict(int)
        for idx in range(len(genres)):
            if genres[idx]==genre:
                tmp[idx]=plays[idx]
        tmp_sort = sorted(tmp.items(),key=lambda x:x[1], reverse=True)

        for i in range(len(tmp_sort)):
            answer.append(tmp_sort[i][0])
            if i==1:
                break

    return answer


solution(["classic","pop","classic","classic","pop","pop"],[500,600,150,800,2500,600])