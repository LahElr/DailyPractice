r'''
基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 'A'、'C'、'G' 和 'T' 之一。

假设我们需要调查从基因序列 start 变为 end 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。

例如，"AACCGGTT" --> "AACCGGTA" 就是一次基因变化。
另有一个基因库 bank 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。（变化后的基因必须位于基因库 bank 中）

给你两个基因序列 start 和 end ，以及一个基因库 bank ，请你找出并返回能够使 start 变化为 end 所需的最少变化次数。如果无法完成此基因变化，返回 -1 。

注意：起始基因序列 start 默认是有效的，但是它并不一定会出现在基因库中。
'''

from collections import deque
from typing import List


def check_conection(gene_a:str,gene_b:str):
    r = 0
    for a,b in zip(gene_a,gene_b):
        if a!=b:
            r+=1
            if r>=2:
                return 0
    if r==1:
        return 1
    return 0

class Solution:

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        #无向图广度优先搜索
        start_id = None
        end_id = None

        for _,g in enumerate(bank):
            if g == startGene:
                start_id = _
            elif g==endGene:
                end_id = _

        l = len(bank)
        if start_id is None:
            bank.append(startGene)
            start_id = l
            l+=1

        if end_id is None:
            return -1

        # graph = [[check_conection(a,b) for a in bank]for b in bank]
        # ↓This is faster
        graph = [[0 for _ in range(l)] for _ in range(l)]
        for i,a in enumerate(bank):
            for j,b in enumerate(bank[i:]):
                j = j+i
                if i == j:
                    graph[i][j] = 1
                else:
                    graph[i][j] = graph[j][i] = check_conection(a,b)
        
        distances = [12 for _ in range(l)] # 0 <= bank.length <= 10
        stack = [start_id]
        distances[start_id] = 0
        while len(stack)>0:
            tgt = stack.pop()
            this_distance = distances[tgt]
            for neighbor,is_edge in enumerate(graph[tgt]):
                if is_edge:
                    compare_distance = distances[neighbor]
                    if compare_distance>this_distance+1:
                        distances[neighbor] = this_distance+1
                        stack.append(neighbor)

        # print(graph)
        ret = distances[end_id]
        if ret<12:
            return ret
        else:
            return -1

start = "AAAAACCC"
end = "AACCCCCC"
bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]

print(Solution().minMutation(start,end,bank))