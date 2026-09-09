from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adjMatrix = defaultdict(list)
        wordList.append(beginWord)

        # build adj matrix
        for word in wordList: # O(n)
            for i in range(len(word)): # O(nm)
                # strings in Python are immutable so we must construct a new one
                pattern = word[:i] + '*' + word[i+1:] # O(nm^2)
                adjMatrix[pattern].append(word)

        # BFS on adj List
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    for adjWord in adjMatrix[pattern]:
                        if adjWord not in visited:
                            visited.add(adjWord)
                            q.append(adjWord)
            res += 1
        return 0