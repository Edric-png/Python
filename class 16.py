# def total_calc(bill_amount,tip_percentage):
#     total = bill_amount*(1+0.01*tip_percentage)
#     total = round(total,2)
#     print (total)
# total_calc(150,20)
# def cube(n):
#     return n*n*n
# def divisible(n):
#     if n %3==0:
#         return cube(n)
#     else:
#         return False
# print(divisible(9))
def func(n):
    if n==0 or n==1:
        return 1
    else:
        return n*func(n-1)
print (func(500))