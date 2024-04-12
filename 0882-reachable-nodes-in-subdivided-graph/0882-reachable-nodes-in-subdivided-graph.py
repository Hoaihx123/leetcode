class Solution(object):
    def reachableNodes(self, edges, maxMoves, n):
        """
        :type edges: List[List[int]]
        :type maxMoves: int
        :type n: int
        :rtype: int
        """
        graph = [{} for _ in range(n)]
        for a, b, v in edges:
            graph[a][b] = v+1
            graph[b][a] = v+1
        visited = set()
        min_current = [10000000 for _ in range(n)]
        min_current[0] = 0
        def find_min(n):
            index, val = -1, 10000000
            for i in range(n):
                if i not in visited and min_current[i] < val:
                    index, val = i, min_current[i]
            return index, val

        s = 0
        check = {}
        while len(visited) < n:
            index, val = find_min(n)
            if index == -1 or val > maxMoves:
                break
            s += 1
            for node in graph[index]:
                if node not in visited:
                    if graph[node][index] + val < min_current[node]:
                        min_current[node] = graph[node][index] + val
                    if graph[node][index] + val - 1 <= maxMoves:
                        s += graph[node][index]-1
                        del graph[node][index]
                    else:
                        check[(index, node)] = maxMoves - val
                else:
                    s += min(graph[index][node]-1, maxMoves - val + check[(node, index)])
                    del check[(node, index)]
            visited.add(index)
        for x in check:
            s += check[x]
        return s
                        
                        
                        
                        
                        
                        