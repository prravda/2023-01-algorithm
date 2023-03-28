from heapq import *
import sys


# def solution(stream: list[int]) -> int:
#     min_heap = [stream[0]]
#     accm_value = stream[0]
#     kth = 1
#
#     for i in range(1, len(stream)):
#         heappush(min_heap, stream[i])
#
#         if i == kth * 3 - 1:
#             accm_value += min_heap[kth - 1]
#             kth += 1
#
#     # add the remaining kth elements to the accumulator
#     accm_value += sum(nsmallest(kth - 1, min_heap))
#
#     return accm_value
#
#
# print(solution([9, 1, 3, 2, 7, 0, -2, 4, 5]))

# serial_input_processed: list[int] = list(map(int, sys.stdin.readline().split()))
# print(solution(serial_input_processed))

"""
가장 적은 값을 가장 빨리 뽑아올 수 있는 data structure - (mean)heap
- stream 이 갱신될 때마다 기본적으로는 meanheap 에 heappush 
- 가장 적은 값을 가져오는 경우엔 heappop

Q. 그런데 그 다음으로 가장 적은 값을 가져오는 경우엔 어떻게 해야할까?

"""

"""
kth 번째로 작다 == (n-k)th 번째로 크다 -> max_heap 활용

"""
def solution(stream: list[int]) -> int:
    max_heap = [-stream[0]]
    result = stream[0]

    for i in range(1, len(stream)):
        kth = i // 3 + 1
        heappush(max_heap, -stream[i])

        till_kth_from_back = []

        for _ in range(len(max_heap) - kth, -1, -1):
            till_kth_from_back.append(heappop(max_heap))

        result += -till_kth_from_back[-1]

        for element in till_kth_from_back:
            heappush(max_heap, element)

    return result


solution([9, 1, 3, 2, 7, 0, -2, 4, 5])


# serial_input_processed: list[int] = list(map(int, sys.stdin.readline().split()))
# print(solution(serial_input_processed))