# class IOString():
#     def __init__(self):
#         self.str1 = ""
#     def get_String(self):
#         self.str1 = input("Enter string:")
#     def print_String(self):
#         print("Result is:",self.str1.upper())
# str1 = IOString()
# str1.get_String()
# str1.print_String()
# class Employee:
#     def _init__(self):
#         print('Employee created')
#     def _del_(self):
#         print("Destructor called")
# def Create_obj():
#     print('Making Object...')
#     obj = Employee()
#     print('function end...')
#     return obj
# print('Calling Create_obj() function...')
# obj = Create_obj()
# print('Program End...')
class pair_elements:
	def twoSum(self, nums, target):
		lookup = {}
		for i, num in enumerate(nums):
			if target - num in lookup:
				return (lookup[target - num], i )
			lookup[num] = i
value = int(input("Enter sum for which you want to make this search : "))
print("index1=%d, index2=%d" % pair_elements().twoSum((10,20,30,40,50,60,70),value))