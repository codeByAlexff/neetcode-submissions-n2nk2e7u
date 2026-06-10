class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:[] for i in range(n)}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = []
        components = 0

        def dfs(node):
            visited.append(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)



        for node in range(n):
            if node not in visited:
                dfs(node)
                components += 1
        return components

        