from collections import defaultdict
from math import ceil


def solution(fees, records):
    data = defaultdict(int)
    parked = {}  # car_number: parked_time
    for record in records:
        time, number, status = map(str, record.split())
        if status == 'IN':
            parked[number] = time
        elif status == 'OUT':
            parked_time = parked[number]
            del parked[number]
            data[number] += (int(time[:2]) - int(parked_time[:2])) * 60 + int(time[3:]) - int(parked_time[3:])

    for number, parked_time in parked.items():
        time = "23:59"
        data[number] += (int(time[:2]) - int(parked_time[:2])) * 60 + int(time[3:]) - int(parked_time[3:])

    temp = []
    for number, total_time in data.items():
        temp.append((number, total_time))
    temp.sort(key=lambda x: x[0])

    answer = []
    for number, total_time in temp:
        if total_time <= fees[0]:
            answer.append(fees[1])
        else:
            total_time -= fees[0]
            answer.append(fees[1] + ceil(total_time / fees[2]) * fees[3])

    return answer
