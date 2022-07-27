def solution(name):
    answer = 0    
    alpha = {"A":0, 'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,
    'L':11,'M':12,'N':13,'O':12,'P':11,'Q':10,'R':9,'S':8,'T':7,'U':6,'V':5,'W':4,'X':3,'Y':2,'Z':1}
    
    name = list(name)
    n = len(name)
    
    for i in name:
        answer += alpha[i]
    
    name[0] = 'A' #첫번째껀 이동비용없이 바꿔버림
    
    for i in range(n):
        
        if name[i]=='A':
            continue
        
        left, right = 1,1
        
        while name[i - left] == 'A':
            left += 1
            
        while i+right <= n-1 and name[i + right] == 'A':
            right += 1
        
        #print(i, left, right)
        answer += left if left < right else right
        name[i] = 'A'
        #print(name)    
    
    return answer