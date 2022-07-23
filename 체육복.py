def solution(n, lost, reserve):
    answer = 0
    # 1<n<31
    # 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. ?
    #중복값 제거 https://velog.io/@daybreak/Python%EC%97%90%EC%84%9C-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%A4%91%EB%B3%B5%EC%A0%9C%EA%B1%B0
    reserve_set = set(reserve)-set(lost)
    lost_set = set(lost)-set(reserve)
    reserve_set2 = set(reserve)&set(lost)
    print(reserve_set2)
    for i in sorted(reserve_set): 
        if i-1 in lost_set: #3-1 lost 2가 있으면 lost_set에있는 목록 제거
            lost_set.remove(i-1)            
        elif i+1 in lost_set:
            lost_set.remove(i+1)        
    #true 일때 answer ++;
    
    return n-len(lost_set)