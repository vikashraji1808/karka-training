# ticket price finding task1

"""age=int(input("enter your age : "))
if age<3:
    print("you get in free")
elif age>=3 and age<=12:
    print("you are pay$10")
elif age>=65:
    print("you are pay$12")
else:
    print("you are pay$15")


days=int(input("enter your day between 1to7 : "))
if days==1:
    print("today is sunday")
elif days==2:
    print("today is monday")
elif days==3:
    print("today is tuesday")
elif days==4:
    print("today is wednesday")
elif days==5:
    print("today is thursday")
elif days==6:
    print("today is friday")
elif days==7:
    print("today is saturday")
else:
    print("invalid day number")"""

# orai printla panuradhu

"""num=int(input("enter your between 1 to 7 : "))
days=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
print(days[num-1])"""

num1=int(input("enter the number1 : "))
num2=int(input("enter the number2 : "))
num3=int(input("enter the number3 : "))
if num1>num2:
    if num1>num3:
        print(num1,"this is largest number ")
    else:
        print(num3,"this is largest number") 
elif num2>num3:
        print(num2,"this is largest number")
elif num3>num2:
    print(num3,"this is largest number")

