# 안 푼 문제
25 기출 실패율


# 정렬 알고리즘 개요

| 정렬: 데이터를 특정한 기준에 따라서 순서대로 나열하는 것

이 책에서는 오름차순을 위한 소스코드만 다룬다

# 선택 정렬(Selection Sort)

데이터가 무작위로 여러 개 있을 때, 이 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복하는 원시적인 방법

- 가장 작은 데이터를 앞으로 보내는 과정을 `N-1` 번 반복하면 정렬이 완료된다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7238c67b-e9d6-4df8-9017-a88b03d61b3e/Untitled.png)
    

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
	min_index = i    # 가장 작은 원소의 인덱스
	for j in range(i+1, len(array)):
		if array[min_index] > array[j]:
			min_index = j
	array[i], array[min_index] = array[min_index], array[i]    # 스와프

print(array)
```

### 선택 정렬의 시간 복잡도

이중 반복문 사용했기 때문에 O(N^2)
매우 느리지만 특정한 리스트에서 가장 작은 데이터를 찾는 일이 잦으므로 익숙해질 필요가 있다.

# 삽입 정렬(Insertion Sort)

데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입하는 알고리즘

- 삽입 정렬은 필요할 때만 위치를 바꾸므로 데이터가 거의 정렬되어 있을 때 훨씬 효율적이다.
- 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다. (첫 번째 데이터는 정렬되어 있다고 가정하고, 두 번째 데이터부터 정렬 시작)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5b30532c-177f-4ce9-8290-d1a1314748f0/Untitled.png)

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
	for j in range(i, 0, -1):    # 인덱스 i부터 1까지 감소하며 반복하는 문법
		if array[j] < array[j - 1]:    # 한 칸씩 왼쪽으로 이동
			array[j], array[j - 1] = array[j - 1], array[j]
		else:    # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
			break
	print(array)
```

### 삽입 정렬의 시간 복잡도

반복문 중첩으로 시간 복잡도는 O(N^2)이지만, 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다.

# 퀵 정렬(Quick Sort)

병합 정렬과 함께, 가장 많이 사용되고 빠른 알고리즘.
기준 데이터를 설정하고, 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸자.

- 피벗: 큰 숫자와 작은 숫자를 교환할 때 교환하는 기준.
- 호어 분할: 리스트에서 첫 번째 데이터를 피벗으로 정한다.

### 파트 1: 피벗 설정하고 분할하기

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e4cbfc16-b766-480f-8e48-343320b5a238/Untitled.png)

가장 왼쪽 데이터 5를 피벗으로 정한다

왼쪽에서부터 5(피벗)보다 큰 데이터 선택 / 오른쪽부터 5(피벗)보다 작은 데이터 선택
그리고 두 데이터의 위치를 서로 변경한다.

이와 같은 과정을 반복

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6d5767d7-211f-498b-be70-28bd55708474/Untitled.png)

반복하다가 위와 같이 찾는 값이 엇갈리는 경우: 작은 데이터(1)과 피벗의 위치(5)를 변경한다
→ 분할 완료

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3f5b4c43-1b60-4fb4-a91e-91c477531c8e/Untitled.png)

`분할` 혹은 `파티션` : 피벗의 왼쪽에는 피벗보다 작은 데이터, 오른쪽에는 큰 데이터가 위치하도록 하는 작업

### 파트 2: 피벗의 왼쪽 리스트에서 다시 정렬하기

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4f295bc5-2c0d-48c0-bb3e-407d147d9c54/Untitled.png)

### 파트 3: 피벗의 오른쪽 리스트에서 다시 정렬하기

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0ac5467b-b520-4cc5-8d28-77bf88525765/Untitled.png)

리스트의 원소가 1이 될 때까지 위의 과정을 반복한다.

```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
	if start >= end:    # 원소가 1인 경우 종료
		return

	pivot = start    # 피벗은 첫 번째 원소
	left = start + 1
	right = end

	while left <= right:
		# 피벗보다 큰 데이터를 찾을 때까지 반복
		while left <= end and array[left] <= array[pivot]:
			left += 1

		# 피벗보다 작은 데이터를 찾을 때까지 반복
		while right > start and array[start] >= array[pivot]:
			right -= 1
		
		if left > right:    # 엇갈렸다면 작은 데이터와 피벗을 교체
			array[right], array[pivot] = array[pivot], array[right]
		else:    # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
			array[left], array[right] = array[right], array[left]

		# 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
		quick_sort(array, start, right-1)
		quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
```

### 퀵 정렬의 시간 복잡도

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e634629c-fd18-49dd-a7e5-20c33176e3ca/Untitled.png)

분할이 이루어지는 횟수가 기하급수적으로 감소하기 때문에 매우 빠르다

⚠️ 평균적으로는 O(NlogN)이지만 최악의 경우 O(N^2)이다. 파이썬은 최악의 경우에도 O(NlogN)를 보장해줌.

- 데이터가 무작위로 입력되는 경우: 퀵 정렬이 더 빠름
- 데이터가 이미 정렬되어 있는 경우: 삽입 정렬이 더 빠름

# 계수 정렬(Count Sort)

특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘.

- 조건: **********************데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때**********************
- 모든 범위를 담을 수 있는 크기의 배열을 선언해야 하기 때문에, **가장 큰 데이터와 가장 작은 데이터의 차이가 너무 크다면 계수 정렬을 사용할 수 없다.**

1. 가장 큰 데이터~가장 작은 데이터의 범위가 모두 담길 수 있는 리스트 1개 생성, 0으로 초기화
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7628e1fd-28e2-407c-b4d5-8a433e0a9a30/Untitled.png)
    
2. 데이터 하나씩 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가시킨다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b86e3a1e-6cb3-4e70-81b1-59106cada624/Untitled.png)
    

```python
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 3, ...]
count = [0] * (max(array) + 1)

for i in range(len(array)):
	count[array[i]] += 1    # 각 데이터에 해당하는 인덱스의 값 증가

# 출력하기
for i in range(len(count)):    # 리스트에 기록된 정렬 정보 확인
	for j in range(count[i]):
		print(i, end=' ')    # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
```

### 계수 정렬의 복잡도 분석

- 계수 정렬의 시간 복잡도와 공간 복잡도는 모두 O(N+K)
N: 데이터 개수, K: 데이터 중 최댓값
- 계수 정렬은 떄에 따라서 심각한 비효율성 초래 (최댓값~최솟값 차이가 극단적으로 많이 나는 경우)
- 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적으로 사용 가능

# 파이썬의 정렬 라이브러리

기본 정렬 라이브러리`sorted()` : 최악의 경우에도 O(NlogN) 보장한다.

- 리스트, 집합, 딕셔너리 → 정렬 후 리스트로 반환
- `result = sorted(array)` 또는 `array.sort()` 로 사용한다.
- key 매개변수에 함수를 넣어서 사용 가능
    
    ex. 튜플의 두 번째 원소를 기준으로 정렬하는 경우
    

파이썬의 정렬 라이브러리는 병합 정렬과 삽입 정렬을 더한 하이브리드 방식을 사용한다.

- 문제에서 별도의 요구가 없이 단순히 정렬하는 상황에서는 기본 라이브러리 사용
- 데이터의 범위가 한정되어 있으며 더 빠르게 동작해야할 때는 계수 정렬 사용’

정렬 알고리즘이 사용되는 경우: 문제 유형 3가지

1. **정렬 라이브러리로 풀 수 있는 문제**
2. **정렬 알고리즘의 원리에 대해 물어보는 문제**: 선택 정렬, 삽입 정렬, 퀵 정렬 등 숙지하기
3. **더 빠른 정렬이 필요한 문제**: 계수 정렬 등 다른 정렬 알고리즘 이용, 알고리즘의 구조적인 개선