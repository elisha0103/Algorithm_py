import sys
input = sys.stdin.readline

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end): #배열, 시작점, 끝점(0번 인덱스와 마지막 인덱스)
    if start >= end: #시작점과 끝점이 같다면 탈출. 결국 원소가 1개일경우 탈출
        return
    pivot = start #피벗은 맨 왼쪽, 시작점
    left = start + 1 #left는 피벗 다음 원소
    right = end #right는 배열 맨 끝 인덱스
    while left <= right: #left와 right가 서로 교차되지 않는 경우 계속 진행
        # left가 끝점에 도달 하지않고, left 값이 피벗 값 이하면 오른 쪽으로 이동
        # left 값이 피벗 값 이상이면 탈출
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # right가 피벗보다는 오른 쪽에 있고, right 값이 피벗 값 이상이면 왼쪽으로 이동 
        # right 값이 피벗 값 이하면 탈출
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 위 연산으로 left와 right 위치가 서로 교차되면
        if left > right: # 작은 값, right 값과 피벗 값이 스와프
            array[right], array[pivot] = array[pivot], array[right]
        else: # left와 right 위치가 서로 교차되지 않으면 단순 left와 right의 값을 스와프
            array[left], array[right] = array[right], array[left]

        quick_sort(array, start, right - 1) # left와 right가 서로 교차된 뒤 왼쪽 리스트 퀵정렬 진행
        quick_sort(array, right + 1, end) #left와 right가 서로 교차된 뒤 오른쪽 리스트 퀵정렬 진행

quick_sort(array, 0, len(array) - 1)
print(array)
