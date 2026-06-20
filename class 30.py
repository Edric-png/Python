# from abc import ABC, abstractmethod
# class Absclass(ABC):
#     def print(self,x):
#         print("Passed value: ", x)
#     @abstractmethod
#     def task(self):
#         print("We are inside Absclass task")
# class test_class(Absclass):
#     def task(self):
#         print("We are inside test_class task")
# test_obj = test_class()
# test_obj.task()
# test_obj.print(100)
# import necessary packages
from abc import ABC, abstractmethod
class Animal(ABC):
	def move(self):
		pass
# sub classes
class Human(Animal):
	def move(self):
		print("I can walk and run")
class Snake(Animal):
	def move(self):
		print("I can crawl")
class Dog(Animal):
	def move(self):
		print("I can bark")
class Lion(Animal):
	def move(self):
		print("I can roar")
R = Human()
R.move()
K = Snake()
K.move()
R = Dog()
R.move()
K = Lion()
K.move()