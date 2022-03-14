from collections import defaultdict

def solution(record):
    dic = defaultdict(str)    # key: user_id, value: nickname
    for s in record:
        split = s.split(' ')
        cmd = split[0]
        if cmd == 'Enter':
            user_id = split[1]
            nickname = split[2]
            dic[user_id] = nickname
        elif cmd == 'Leave':
            continue
        else:   # Change
            user_id = split[1]
            nickname = split[2]
            dic[user_id] = nickname

    answer = []
    for s in record:
        split = s.split(' ')
        cmd = split[0]
        if cmd == 'Enter':
            user_id = split[1]
            answer.append(dic[user_id] + '님이 들어왔습니다.')
        elif cmd == 'Leave':
            user_id = split[1]
            answer.append(dic[user_id] + '님이 나갔습니다.')
        else:   # cmd == 'Change'
            continue

    return answer
