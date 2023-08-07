"""a=int(input("enter your number : ")) 
b=a%2
if b==0:
    print("it is a even number")
else:
    print("it is a odd number")"""

"""a=int(input("enter your number : "))
b=int(input("enter your number2 : "))
c=a%b
if c==0:
    print("yes it is possible")
else:
    print("no it is not possible")"""
year=int(input("enter year : "))
if (year%400==0 and year%100==0)or(year%4==0 and not year%100==0):
    print("this is leapyear")
else:
    print("this is not leapyear")