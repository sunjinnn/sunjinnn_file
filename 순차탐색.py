# 순차탐색 함수 정의
def sequential_search(A, key):
    # 리스트 A를 처음부터 끝까지 반복하며 탐색합니다.
    for i in range(len(A)):
        # 현재 원소와 찾고자 하는 키 값이 일치하면 해당 인덱스를 반환합니다.
        if A[i] == key:
            return i
    # 탐색이 끝나도 일치하는 원소를 찾지 못했으면 -1을 반환합니다.
    return -1

# 사용 예시 리스트와 찾고자 하는 키 값을 정의합니다.
A = [64, 25, 12, 22, 11]
key = 22

# 순차탐색 함수 호출하여 결과를 저장합니다.
result = sequential_search(A, key)

# 결과에 따라 메시지를 출력합니다.
if result != -1:
    print(f"Element found at index {result}")  # 원소를 찾았을 때 해당 인덱스 출력
else:
    print("Element not found in the list.")  # 원소를 찾지 못했을 때 메시지 출력