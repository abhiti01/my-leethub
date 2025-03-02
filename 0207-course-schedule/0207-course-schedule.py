class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i):
            print(i)
            if visited[i] == 1:
                return True
            if visited[i] == -1:
                return False
            visited[i] = -1
            for val in graph[i]:
                if not dfs(val):
                    return False
            visited[i] = 1
            return True
    
        visited = [0 for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]
        print(graph)
        
        for value in prerequisites:
            course, prereq = value
            print(course,prereq)
            graph[course].append(prereq)
            
        print(graph)
            
        
        for i in range (len(prerequisites)):
            if not dfs(prerequisites[i][0]):
                return False
            
        return True