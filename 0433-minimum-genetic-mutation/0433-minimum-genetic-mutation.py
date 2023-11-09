class Solution:
    from collections import deque

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        genes = deque([(startGene, 0)])
        seen = {startGene}
        
        while genes:
            node, steps = genes.popleft()
            if node == endGene:
                return steps
        
            for char in "AGCT":
                for i in range(len(node)):
                    neighbor = node[:i] + char + node[i+1:]
                    if neighbor not in seen and neighbor in bank:
                        genes.append((neighbor, steps+1))
                        seen.add(neighbor)
        return -1
            
