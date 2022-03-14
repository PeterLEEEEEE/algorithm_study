def solution(record):
    answer = []    
    stringHash = {}
    
    for r in record:
        r = r.split()
        if r[0] == 'Enter':
            answer += [[r[1], '님이 들어왔습니다.']]
            stringHash[r[1]] = r[2]
        elif r[0] == 'Change':
            stringHash[r[1]] = r[2]
        else:
            answer += [[r[1], '님이 나갔습니다.']]
    
    n = len(answer)
    for i in range(n):
        x = answer[i]
        nick_name = stringHash[x[0]]
        answer[i] = ''.join([nick_name, x[1]])

    return answer