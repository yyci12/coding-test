def solution(s):
    answer = -1
    stack = []
    #bacaacab 
    for i in range(len(s)):
        if (len(stack) == 0) : # stack 리스트가 0일경우 stack에 s[i]를 추가
            stack.append(s[i])
        else: #stack에 값이 있을경우
            if stack[-1] == s[i]: # stack list의 끝값을 비교해서 s[i]와 같을경우 stack을 제거
                stack.pop()
            else: #아닐경우 append
                stack.append(s[i])
    if(len(stack) > 0) : #스택에 결국 값이 남아있을경우 return 0;
        return 0;
    else:
        return 1;