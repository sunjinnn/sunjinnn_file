def insertion_sort(A):
    """
    주어진 리스트를 삽입 정렬을 사용하여 정렬합니다.
    
    Parameters:
    - A: 정렬할 리스트
    
    Returns:
    - None (리스트가 직접 정렬됩니다)
    """
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        
        # key보다 큰 원소들을 오른쪽으로 이동하여 적절한 위치에 key를 삽입합니다.
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        
        # key를 올바른 위치에 삽입합니다.
        A[j + 1] = key
        
        # 정렬 중간 과정을 출력하는 함수 호출
        printStep(A, i)

def printStep(A, step):
    """
    현재 정렬 중간 과정을 출력합니다.
    
    Parameters:
    - A: 리스트
    - step: 현재 정렬된 부분의 끝 인덱스
    
    Returns:
    - None
    """
    print("Step %2d: %s" % (step, A))

# 사용 예시
A = [64, 25, 12, 22, 11]
insertion_sort(A)