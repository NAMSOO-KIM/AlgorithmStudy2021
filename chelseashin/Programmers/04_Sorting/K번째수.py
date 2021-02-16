# 5분 소요
# 문제 읽고 그대로 구현
# List Comprehension 으로 한줄 코딩

def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i, j, k in commands]

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))