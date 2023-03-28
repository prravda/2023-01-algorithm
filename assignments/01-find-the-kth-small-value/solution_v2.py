import sys
import heapq

def solution(stream: list[int]) -> int:
    max_heap = []
    accm_value = 0

    for i in range(len(stream)):
        kth = i // 3 + 1
        heapq.heappush(max_heap, -stream[i])

        till_kth_desc = []

        for _ in range(kth):
            till_kth_desc.append(-heapq.heappop(max_heap))

        accm_value += till_kth_desc[-1]

        for element in till_kth_desc:
            heapq.heappush(max_heap, -element)

    return accm_value




# serial_input_processed: list[int] = list(map(int, sys.stdin.readline().split()))
# print(solution(serial_input_processed))