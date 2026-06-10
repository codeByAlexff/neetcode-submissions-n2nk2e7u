class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #Create and adjacency list
        adj = {i:[] for i in range(numCourses)}

        #Map each course to its prerequisites
        for course, preCourse in prerequisites:
            adj[course].append(preCourse)
        
        #Initialize a visiting variable as a set to store all courses along the dfs path
        visiting = set()

        #Initialize depth first search inside course
        def dfs(course):
            #If course is already visited then a cycle is detected
            if course in visiting:
                return False
            #If adjacency list is empty return True
            if adj[course] == []:
                return True
            
            #Add course to visited if neither of the above
            visiting.add(course)

            #Loop through precourses
            for preCourse in adj[course]:
                #If precourse CANT be completed
                if not dfs(preCourse):
                    return False
            #If it CAN be completed
            #Remove first appearance of course from visiting
            visiting.remove(course)
            #Make courses empty
            adj[course] = []
            #Return True
            return True
        
        #Loop through numCourses
        for c in range(numCourses):
            #Check if dfs CANT be completed
            if not dfs(c):
                return False
        #If it CAN be completed return True
        return True



