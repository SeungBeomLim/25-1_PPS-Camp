# B034. 체육복 - Programmers

def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    for student in sorted(lost_set):
        if student - 1 in reserve_set:
            reserve_set.remove(student - 1)
            lost_set.remove(student)
        elif student + 1 in reserve_set:
            reserve_set.remove(student + 1)
            lost_set.remove(student)
    
    return n - len(lost_set)