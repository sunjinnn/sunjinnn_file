def dfs(graph, start, visited):
    """
    깊이 우선 탐색(DFS) 알고리즘을 사용하여 그래프를 탐색하고 방문한 노드를 출력합니다.
    
    Parameters:
    - graph: 탐색할 그래프를 나타내는 인접 리스트 (딕셔너리 형태)
    - start: 탐색을 시작할 노드
    - visited: 방문한 노드를 기록하는 집합(set) 객체
    
    Returns:
    - None
    """
    
    # 현재 노드가 방문되지 않았다면 방문한 노드에 추가하고 출력합니다.
    if start not in visited:
        visited.add(start)
        print(start, end=' ')
        
        # 현재 노드와 연결된 이웃 노드들을 가져옵니다.
        nbrs = graph[start]
        
        # 이웃 노드들 중에서 아직 방문하지 않은 노드에 대해 재귀적으로 DFS를 호출합니다.
        for v in nbrs:
            if v not in visited:
                dfs(graph, v, visited)

# 예시 그래프 (인접 리스트 형태로 표현)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# 방문한 노드를 기록하기 위한 빈 집합을 생성합니다.
visited = set()

# DFS 함수 호출 및 결과 출력
print("DFS 탐색 결과:")
dfs(graph, 'A', visited)