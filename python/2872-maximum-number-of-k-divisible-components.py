class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :type k: int
        :rtype: int
        """

        connections = dict()
        for n0, n1 in edges:
            connections.setdefault(n0, set()).add(n1)
            connections.setdefault(n1, set()).add(n0)

        visited = set()
        components_count = 0
        
        def dfs(node):
            if node in visited:
                return 0
            nonlocal components_count
            
            visited.add(node)
            tree_sum = values[node]
            
            for child in connections.get(node, []):
                if child in visited: 
                    continue
                
                child_sum = dfs(child) % k
                if child_sum == 0:
                    components_count += 1
                    continue

                tree_sum += child_sum

            return tree_sum
        
        # dfs(0)

        if dfs(0) % k == 0:
            components_count += 1

        return components_count
            