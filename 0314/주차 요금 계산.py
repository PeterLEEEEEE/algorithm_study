from collections import defaultdict
from math import ceil

def solution(fees, records):
    dic_records = defaultdict(int)
    for r in records:
        t, n, IO = r.split()
        if IO == "IN":
            dic_records[int(n)] -= int(t[:2]) * 60 + int(t[3:])
        else:
            dic_records[int(n)] += int(t[:2]) * 60 + int(t[3:])
    
    for k, v in dic_records.items(): 
        if v <= 0:
            dic_records[k] += 23 * 60 + 59

    dic_fee = defaultdict(int) 
    for k, v in dic_records.items():
        if v <= fees[0]:
            dic_fee[k] = fees[1]
        else:
            dic_fee[k] = fees[1] + fees[3] * ceil((v - fees[0])/fees[2])
    
    return [value for key, value in sorted(dic_fee.items())]