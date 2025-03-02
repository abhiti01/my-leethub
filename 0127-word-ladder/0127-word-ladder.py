class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        neighbours = collections.defaultdict(list)
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                neighbours[pattern].append(word)
        res=1
        q = deque()
        visit=set([beginWord])
        q.append(beginWord)
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j]+"*"+word[j+1:]
                    for neighbour in neighbours[pattern]:
                        if neighbour not in visit:
                            visit.add(neighbour)
                            q.append(neighbour)
            res+=1
        return 0