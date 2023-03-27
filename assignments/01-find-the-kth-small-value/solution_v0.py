import heapq
import sys

serial_input_processed: list[int] = list(map(int, sys.stdin.readline().split()))


def solution(serial_input: list[int]) -> int:
    heap_queue = []
    heapq.heapify(heap_queue)

    accm_value = 0

    for i in range(len(serial_input)):
        kth = i // 3 + 1
        heapq.heappush(heap_queue, serial_input[i])

        till_kth_desc: list[int] = []

        for _ in range(kth):
            till_kth_desc.append(heapq.heappop(heap_queue))

        accm_value += till_kth_desc[-1]

        for element in till_kth_desc:
            heapq.heappush(heap_queue, element)

    return accm_value


print(solution(serial_input_processed))
