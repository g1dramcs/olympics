def count_ways_to_build_road(n, k, roads): 
    from collections import defaultdict 

    graph = defaultdict(list) 
    for u, v in roads: 
        graph[u].append(v) 
        graph[v].append(u) 

    def dfs(node, parent): 
        subtree_size[node] = 1 
        for neighbor in graph[node]: 
            if neighbor == parent: 
                continue 
            dfs(neighbor, node) 
            subtree_size[node] += subtree_size[neighbor] 

    subtree_size = [0] * (n + 1) 
    dfs(1, -1) 

    result = 0 
    for u in range(1, n + 1): 
        for v in graph[u]: 
            if subtree_size[u] < subtree_size[v]: 
                size1 = subtree_size[u] 
                size2 = n - size1 
            else: 
                size1 = subtree_size[v] 
                size2 = n - size1 

            if k - 1 <= size1 and k - 1 <= size2: 
                result += 1 

    return result 

n, k = map(int, input("Введите количество ключевых пунктов и размер цикла через пробел: ").split()) 
roads = [] 
print(f"Введите {n - 1} дороги в формате 'u v':") 
for _ in range(n - 1): 
    u, v = map(int, input().split()) 
    roads.append((u, v)) 

result = count_ways_to_build_road(n, k, roads) 
print(f"Количество способов: {result}") 
