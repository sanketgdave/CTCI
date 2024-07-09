from collections import deque

class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        students = deque(students)
        sandwiches = deque(sandwiches)

        while sandwiches and students:
            if students[0] == sandwiches[0]:
                students.popleft()  # The student takes the sandwich and both leave the queue
                sandwiches.popleft()
            else:
                # Check if no students want the sandwich at the front of the queue
                if all(student != sandwiches[0] for student in students):
                    break  # No student can eat the sandwich at the front, exit loop
                # Otherwise, rotate the queue
                students.append(students.popleft())

        return len(students)