"""
[ Author ]
201603001 전인섭

[ Structure ]
- 두 개의 함수로 나누어 문제를 풀어낼 수 있고, 두 개의 함수가 밀접한 관계를 갖고 있어 class 로 묶었습니다.
- 해당 문제는 구간을 가운데(mid_index) 를 기준으로 하여 왼쪽/오른쪽으로 나눈 뒤에
  각 구간의 부분합 중 가장 큰 값을 재귀적으로 구하는 함수와
  가운데를 포함한(crossing_mid) 부분합을 구하는 함수로 나눌 수 있지만,
  하나의 함수에 모두 담기엔 함수가 하나 이상의 일을 한다고 생각하여 두 개로 나누었습니다.
- 그리고, 결국 필요한 건 최대 구간합이기 떄문에,
  최대 구간합의 경우 중 하나인 가운데를 포함한 경우의 부분합 함수는
  함수 내부에서 호출하는 또 다른 함수일 뿐, 외부에서 호출할 필요가 없다 생각하여
  `__` 를 통해 private method 처리를 하였습니다.

------------------------------------------------------------------------

[ Description ]
- `max_subarray` 함수는 분할정복 알고리즘 개요에 나온 것처럼 부분합을 구하는 것을 세 개의 경우로 나누어 재귀적으로 처리합니다.
  - 0. mid 기준 왼쪽에 가장 큰 부분합이 존재한다.
  - 1. mid 기준 오른쪽에 가장 큰 부분합이 존재한다.
  - 2. 부분합이 mid 에 걸쳐서 존재한다.
- 재귀함수가 재귀연산을 멈추는 base case 로 element 가 1개일 경우를 설정하였고
  해당 조건일 경우 0번째 element 를 반환하게 처리하였습니다.
- 0, 1번의 경우는 말씀하신 것처럼 재귀적으로 처리하였고, 2번의 경우는
  - 0~mid_index 까지의 부분합 중 최댓값
  - mid_index+1 ~ len(arr) 까지의 부분합 중 최댓값
  을 구한 뒤 이 둘을 더하여 반환하게 처리하였습니다.
- 그리고 0, 1, 2 중 가장 큰 값이 가장 큰 부분합이기에, `max` 함수를 통해 가장 큰 값을 반환하였습니다.

------------------------------------------------------------------------

[ Recurrence relation ]
T(n) = 2*T(n/2) + O(n)

2*T(n/2): 이 문제는 같은 일을 하는 문제 2개로 나눌 수 있습니다.
O(n): 그리고 문제가 나누어 질 때마다 mid_index 를 가로지르는 경우의 최대 부분합을 구해야 합니다.
      왼쪽의 부분합을 계속해서 더하고 오른쪽의 부분합을 계속해서 더하는 과정이 필요한데
      이는 nested 되지 않은 for loop 이 2번 수행되기에 결론적으로 추가되는 연산을 Big-O notation 으로 나타내면 O(n) 입니다.

그리고 분할정복(divide and conquer)의 점화식은 하나의 문제를 더 작은 문제로 나누었을 때의 관계와, 그 때 추가적인 연산의 비용의 합입니다.
따라서 점화식은 위와 같습니다.

------------------------------------------------------------------------

[ Time complexity ]
O(nlog(n))

솔직히 말해서 O(n^2) 보단 더 적은 연산을, O(n) 보단 더 많은 연산을 하기에 O(nlogn) 이라고 생각해 적었습니다...
어떻게 교수님이 말씀해주신 귀납법을 사용해서 증명을 하려 시도해 보았는데, 잘 되지 않습니다.
다음 수업 시간에 한 번만 더 보여주시면... 너무 감사하겠습니다.

"""
class MaximumSubArray:
    def __init__(self):
        # set an integer type infinite value
        self.INT_MAX: int = 999_999_999_999

    def __max_crossing_mid_subarray(self, arr: list[int], mid_index=int) -> int:
        left_sum = -self.INT_MAX
        temp_sum_left = 0

        for i in range(mid_index - 1, -1, -1):
            temp_sum_left += arr[i]
            left_sum = max(left_sum, temp_sum_left)

        right_sum = -self.INT_MAX
        temp_sum_right = 0

        for i in range(mid_index, len(arr)):
            temp_sum_right += arr[i]
            right_sum = max(right_sum, temp_sum_right)

        return left_sum + right_sum

    def max_subarray(self, arr: list[int]) -> int:
        if len(arr) == 1:
            return arr[0]

        mid = len(arr) // 2

        # case 0: when the max subarray is located in left side
        left_max = self.max_subarray(arr[:mid])
        # case 1: when the max subarray is located in right side
        right_max = self.max_subarray(arr[mid:])
        # case 2: when the max subarray is located crossing left and right
        crossing_max = self.__max_crossing_mid_subarray(arr, mid)

        return max(left_max, right_max, crossing_max)


# driver codes
def max_sum(A: list[int], left: int, right: int):
    # A[left], ..., A[right] 중 최대 구간 합 리턴
    instance = MaximumSubArray()
    return instance.max_subarray(A[left:right + 1])


A = [int(x) for x in input().split()]
sol = max_sum(A, 0, len(A) - 1)
print(sol)
