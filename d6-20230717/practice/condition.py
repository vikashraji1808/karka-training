"""gender="female"
if gender=="male":
    print("blue")
else:
    print("pink")

gender=input("enter gender : ")
if gender=="male":
    print("blue")
elif gender=="female":
    print("pink") 
elif gender=="transgender":
    print("lavender")
else:
    print("invalid input")"""

total_marks=int(input("enter total_mark : "))
if total_marks>92:
    print("you are eligible for MBBS")
elif total_marks>85 and total_marks<=92:
    print("you are eligible for BDS")
elif total_marks>75 and total_marks<=85:
    print("you are eligible for agri")
else:
    print("you are eligible for engi")
