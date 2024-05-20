from collections import defaultdict
def solution(clothes):
    c_dict = defaultdict(list)
    for i in clothes:
        c_dict[i[1]].append(i[0])
    total = 1
    for i in c_dict.values():
        total *= len(i)+1
    return total-1
