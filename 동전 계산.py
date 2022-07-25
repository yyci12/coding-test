def solution(money):
    answer = 0
    change = [500, 100, 50, 10]
    remain = money
    for i in change:
        answer += remain //  i
        print(answer)
        remain = remain %  i


    #print(answer)
    return answer

print(solution(2240))

