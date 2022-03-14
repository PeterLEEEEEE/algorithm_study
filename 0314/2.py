from collections import defaultdict


def solution(clothes):
    dic = defaultdict(int)
    for cloth in clothes:
        cloth_type = cloth[1]
        dic[cloth_type] += 1

    answer = 1
    for type in dic.keys():
        answer *= (dic[type] + 1)
    answer -= 1  # 어떤 종류의 옷도 선택하지 않는 경우

    return answer
