import queue

def bfs(graph, start):
    """
    너비 우선 탐색(BFS) 알고리즘을 사용하여 그래프를 탐색하고 방문한 노드를 출력합니다.
    
    Parameters:
    - graph: 탐색할 그래프를 나타내는 인접 리스트 (딕셔너리 형태)
    - start: 탐색을 시작할 노드
    
    Returns:
    - None
    """
    
    # 방문한 노드를 기록하기 위한 집합(set) 객체를 생성하고 시작 노드를 추가합니다.
    visited = {start}
    
    # 큐(queue)를 생성하고 시작 노드를 enqueue 합니다.
    que = queue.Queue()
    que.put(start)
    
    # 큐가 비어있지 않은 동안 반복합니다.
    while not que.empty():
        # 큐에서 노드를 dequeue하고 출력합니다.
        v = que.get()
        print(v, end=' ')
        
        # 현재 노드와 연결된 이웃 노드들을 가져옵니다.
        nbrs = graph[v]
        
        # 이웃 노드들 중에서 아직 방문하지 않은 노드에 대해 방문 처리하고 큐에 enqueue 합니다.
        for u in nbrs:
            if u not in visited:
                visited.add(u)
                que.put(u)

# 예시 그래프 (인접 리스트 형태로 표현)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# BFS 함수 호출 및 결과 출력
print("BFS 탐색 결과:")
bfs(graph, 'A')