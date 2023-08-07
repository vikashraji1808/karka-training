"""
def hello():
    print("hello welcome")
hello()
frist=0
last=0
def combine_name():
    frist="vikash "
    last="raj"
    print(frist + last)
combine_name()

frist_name=0
second_name=0
def combine_name(v,r):   
    print(v+" "+r)
frist_name=input("enter your first name :")
second_name=input("enter your second name :")
combine_name(frist_name,second_name)
"""

"""def finding_colour(gender):
    if gender=="male":
        print("your are blue colour")
    elif gender=="female":
        print("your are pink colour")
    else:
        print("invalid")

get_gender=input("enter your gender :")
finding_colour(get_gender)"""

def finding_maxmim(num1,num2):
    if num1>num2:
        finding_oddeven(num1)
        print(num1," is the maximum")
    elif num2>num1:
        finding_oddeven(num2)
        print(num2," is the maximum")
    elif num1==num2:
        print("it is equal")



def finding_oddeven(max_num):
    if max_num%2==0:
        print(max_num," is even number")
    else:
        print(max_num," is odd number")

get_number1=int(input("enter the number :"))
get_number2=int(input("enter the number :"))
finding_maxmim(get_number1,get_number2)
















