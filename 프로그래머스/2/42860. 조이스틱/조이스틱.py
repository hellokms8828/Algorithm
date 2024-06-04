def count_initial_A(s):
    count = 0
    for char in s:
        if char == 'A':
            count += 1
        else:
            break
    return count

def solution(name):
    if name == len(name)*"A":
        return 0
    alpha = [ chr(65 + i) for i in range(26)]
    count = 0
    
    for i in range(len(name)):
        curIdx = 0
        tarIdx=alpha.index(name[i])
        rGap = abs(26 - (tarIdx - curIdx))
        lGap = tarIdx - curIdx
        
        gap = min(lGap, rGap)
        curIdx = tarIdx
        count += gap
        
    move = len(name) - 1

    for i in range(len(name)):
        next_i = i + 1
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        distance = min(i, len(name) - next_i)
        move = min(move, i + len(name) - next_i + distance)

    return count + move
