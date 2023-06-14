def solution(number):
    if number < 0:
        return 0
    l = []
    for i in range(number):
        l.append(i)
    l_elig = list(map(lambda x: x if not x % 3 or not x % 5 else 0, l))
    return sum(l_elig)
