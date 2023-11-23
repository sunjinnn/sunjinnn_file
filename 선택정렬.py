# 선택 정렬 함수 정의
def selection_sort(A):
    # 리스트의 길이를 가져옵니다.
    n = len(A)
    
    # 리스트의 마지막 원소를 제외한 모든 원소에 대해 반복합니다.
    for i in range(n - 1):
        # 현재 인덱스를 가장 작은 값의 인덱스로 설정합니다.
        least = i
        
        # 현재 인덱스 다음 위치부터 리스트의 끝까지 반복합니다.
        for j in range(i + 1, n):
            # 최솟값을 찾습니다.
            if A[j] < A[least]:
                least = j
        
        # 현재 인덱스와 최솟값의 위치를 교환합니다.
        A[i], A[least] = A[least], A[i]
        
        # 현재 단계에서의 리스트 상태를 출력하는 함수를 호출합니다.
        printStep(A, i + 1)

# 리스트와 현재 단계를 받아 리스트의 현재 상태를 출력하는 함수 정의
def printStep(A, step):
    # Step 번호와 현재 리스트를 포맷에 맞춰 출력합니다.
    print("Step %2d: %s" % (step, A))

# 사용 예시: 정렬하고자 하는 초기 리스트를 정의하고, 선택 정렬 함수를 호출합니다.
A = [64, 25, 12, 22, 11]
selection_sort(A)