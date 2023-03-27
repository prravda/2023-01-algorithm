import heapq
import sys


def solution(stream: list[int]) -> int:
    min_heap = []
    accm_value = 0

    for i in range(len(stream)):
        kth = i // 3 + 1
        heapq.heappush(min_heap, stream[i])

        till_kth_asc: list[int] = []
        copied_min_heap = [_ for _ in min_heap]

        for _ in range(kth):
            till_kth_asc.append(heapq.heappop(copied_min_heap))

        accm_value += till_kth_asc[-1]

    return accm_value


serial_input_processed: list[int] = list(map(int, sys.stdin.readline().split()))
print(solution(serial_input_processed))