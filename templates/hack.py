# import calendar
# year = 2022
# month = 6
# print(calendar.month(year,month))
###########################################
# a = ['sheep','sheep','sheep','wolf','sheep']
# def qwerty(a):
#     for i in a:
#         if 'wolf' in i:
#             return True
#         else:
#             return False
# print(qwerty(a))
first = int(input('num1: '))
second = int(input('num2: '))
oper = input('operation: ')
def calculate(first,second,oper):
    if oper =='+':
        return first + second
    elif oper == '-':
        return first-second
    elif oper == '*':
        return first*second
print(calculate(first,second,oper))
