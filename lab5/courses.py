#!/usr/bin/env python3 -tt

from datetime import date
from functools import total_ordering

@total_ordering
class Course:
    def __init__(self, department, number, title, *instructors):
        self.department = department
        self.number = number
        self.title = title
        self.instructors = list(instructors)
        self.attendance = {}
    
    def mark_attendance(self, *students):
        self.attendance[date.today()] = set(students)
    def is_present(self, student):
        return student in self.students
    def number_intvalue(self):
        if type(self.number) == str:
            return int(''.join(list(filter(str.isnumeric, self.number))))
        else:
            return self.number
    def __lt__(self, other):
        if self.department != other.department:
            return NotImplemented
        return self.number_intvalue() < other.number_intvalue()
    def __eq__(self, other):
        if self.department != other.department:
            return NotImplemented
        #Note: not number.int_value. 106a and 106b should not necessarily
        # be counted as equal for the purpose of prerequisites.
        return self.number == other.number

class CSCourse(Course):
    def __init__(self, department, number, title, recorded=False):
        super().__init__(department, number, title)
        self.is_recorded = recorded


"""
Assess the following equalities in your Python interpreter. You can import both classes by running either one of the following lines in your terminal

>>> from courses import Course, CSCourse
>>> a = Course("CS", "106A", "Programming Methodology")
>>> b = CSCourse("CS", "106B", "Programming Abstractions")
What is the output of the statements below?

1. type(a)
# <class 'courses.Course'>
2. isinstance(a, Course)
# True
3. isinstance(b, Course)
# True
4. type(a) == type(b)
False
5. a == b
False

As predicted for all.

Further tests for debugging/testing
"""
cs41a = Course("CS", "41A", "Intro to Python", "Sam", "Jerry")
cs41alias = Course("CS", "41A", "The hap.py coder")

cs106a = Course("CS", "106A", "Programming Methodology", "Mehran", "Keith")
cs106a = Course("CS", "106A", "Programming Methodology", "Mehran", "Keith")
cs106b = CSCourse("CS", "106B", "Programming Abstractions")
cs107 = CSCourse("CS", "107", "Computer Organzation and Systems")
cs110 = CSCourse("CS", "110", "Principles of Computer Systems")
econ101 = Course("Econ", "101", "Economic Abstractions")
#False
# Is this desired?
cs106a == cs106b
#TypeError: '<' not supported between instances of 'Course' and 'Course'
# Is this desired?
econ101 == cs106a
# True, as desired
cs110 > cs106b
# False, as desired
cs107 > cs110
# True, as desired
cs41a == cs41alias
# False, as desired
cs106a == cs106b
