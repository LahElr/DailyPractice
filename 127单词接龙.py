from collections import defaultdict, deque
from typing import List
from Trie import TrieWithIDTracking as Trie



class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # build word indexing
        words = Trie()
        words.try_to_add(beginWord)
        for input_word in wordList:
            words.try_to_add(input_word)
        end_id = words.get(endWord)
        if end_id is None:
            return 0

        # build map
        edges = defaultdict(set)

        for word in wordList + [beginWord]:
            id1 = words.get(word)
            chars = list(word)
            for i in range(len(chars)):
                ch = chars[i]
                chars[i] = "*"
                new_word = "".join(chars)

                id2 = words.try_to_add(new_word)
                edges[id1].add(id2)
                edges[id2].add(id1)
                chars[i] = ch

        dis = [float("inf") for _ in range(len(words))]
        dis[0] = 0

        queue = deque([0])
        while queue:
            x = queue.popleft()
            if x == end_id:
                return dis[end_id] // 2 + 1
            for it in edges[x]:
                if dis[it] == float("inf"):
                    dis[it] = dis[x] + 1
                    queue.append(it)

        return 0
