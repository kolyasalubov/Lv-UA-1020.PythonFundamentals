# def solution(number):
#     sum_ = 0
#     if number < 0:
#         return 0
#     for item in range(number):
#         if item % 3 == 0 or item % 5 == 0:
#             sum_ = sum_ + item
#     return sum_
def solution(number):
    return sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0])
print(solution(16))
