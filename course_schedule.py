# Approach:
# 1. Build indegree array to count prerequisites for each course and an adjacency list to map each course to its dependent courses.
# 2. Add all courses with 0 prerequisites to the queue and perform BFS (Kahn's Algorithm for Topological Sort).
# 3. For each course taken, reduce the indegree of its dependent courses. If indegree becomes 0, add it to the queue. 
#    If the total courses processed equals numCourses, return True, else False.

# Time Complexity: O(V + E) — V is numCourses (vertices), E is the number of prerequisites (edges)
# Space Complexity: O(V + E) — For indegree array, adjacency list, and queue

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        dep_arr = [0] * numCourses  # stores indegree (number of prerequisites) of each course

        # Build indegree array
        for i in range(len(prerequisites)):
            dep_arr[prerequisites[i][0]] += 1

        q = deque()
        
        # Add courses with 0 indegree to the queue
        for i in range(numCourses):
            if dep_arr[i] == 0:
                q.append(i)

        adj_list = defaultdict(list)

        # Build adjacency list
        for i in range(len(prerequisites)):
            adj_list[prerequisites[i][1]].append(prerequisites[i][0])

        count = 0

        # BFS
        while q:
            sub = q.popleft()
            count += 1
            dependent = adj_list[sub]

            for i in range(len(dependent)):
                dep_arr[dependent[i]] -= 1

                if dep_arr[dependent[i]] == 0:
                    q.append(dependent[i])
        
        return count == numCourses
