# Author
- 201603001 전인섭

# Description
## Data structure
- `heap`

## Algorithm
### TL;DR
- 가장 작은 수를 빠르게 뽑아내는 게 문제 해결에 도움이 된다고 생각하여, `mean heap` 을 사용하였다.
### Detail 
- for loop 을 통해 stream 을 index 를 기준으로 순회한다. 그리고 이 for loop 안에서 아래와 같은 과정들을 수행한다.
    - 각 stream 의 element 를 `heappush` 로 heap 에 추가한다.
    - list comprehension 으로 heap 을 복사한다.
    - 복사한 heap 으로부터 k 번 만큼 `heappop` 연산을 수행해 k 번째 작은 수를 찾아낸다.
    - 해당 k 번째 작은 수를 `accm_value` 라는 값에 더한다.
- for loop 순회가 완료된 후, accm_value 라는 결과값을 반환한다. 

## Time complexity analysis
### TL;DR
- `O(nlogn)`
### Detail
- 먼저 for loop 로 stream 의 모든 element 를 순회해야 하기에 n 번의 연산이 필요하다. 그리고 이 loop 안에서 다음과 같은 연산들이 이뤄진다.
  - kth 의 계산 
  - kth 만큼 해당 과정을 반복한다.
    - heapq module 의 heappush (logN)
    - heapq module 의 heappop (logN)
- 이렇게 되면 for loop 안의 for loop 은 k*logN, 그리고 바깥의 for loop 인 n 과 곱해져 nlogN time complexity 가 나오게 된다.