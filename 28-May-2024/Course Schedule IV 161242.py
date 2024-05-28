# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        courses = defaultdict(list)
        isReachable = [[False] * numCourses for _ in range(numCourses)]
        indegree = [0] * numCourses

        for prereq, cour in prerequisites:
            courses[prereq].append(cour)
            indegree[cour] += 1
        
        qeue = deque([i for i in range(numCourses) if indegree[i] == 0])

        while qeue:
            curr_cours = qeue.popleft()

            for next_course in courses[curr_cours]:
                isReachable[curr_cours][next_course] = True
            
                for course in range(numCourses):
                    isReachable[course][next_course] = isReachable[course][next_course] or isReachable[course][curr_cours]
                
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    qeue.append(next_course)
        
        return [isReachable[start][end] for start, end in queries]

        