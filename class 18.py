# try:
#     a = int(input("Enter any number:"))
#     print(a)
# except ValueError as ex:
#     print(ex)
# try:
#     a=int(input("Enter any number:"))
#     b=int(input("Enter any number:"))
#     c=a/b
#     print(c)
# except ZeroDivisionError as ex:
#     print(ex)
# except SyntaxError as ex:
#     print(ex)
# finally:
#     print("This will run for sure")
# a = False
# while not a:
#     try:
#         b = int(input("Enter any number:"))
#         while b%2==0:
#             print("Bye")
#         a = True
#     except ValueError as ex:
#         print(ex)