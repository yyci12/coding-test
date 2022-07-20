def solution(s):
    answer = True
    stack = []
    if(s[0] == ")" or s[-1]=="("):
        return False;
    for i in range(len(s)):
        if(len(stack) == 0):
            stack.append(s[i])
        else:
            if(stack[-1] == "(" and s[i] == ")"):
                stack.pop()
            else:
                stack.append(s[i])
        
    if(len(stack) > 0) : #스택에 결국 값이 남아있을경우 return 0;
        return False;
    else:
        return True;
    