## Hackerrank Python Certification Solution

"""
1. Python: Average Function
"""

from statistics import mean

def avg(*num1):
	return mean(num1)


##################################################
"""
2. Python: Shape classes with Area Method
"""

class Rectangle:
	def __init__(self, length, breadth):
		self.length = length
		self.breadth = breadth
	def area(self):
		return self.length*self.breadth

class Circle:
	def __init__(self, radius):
		self.radius = radius
	def area(self):
		# return 3.14*self.radius*self.radius
		return math.pi*self.radius*self.radius
