user_foods1=(input("enter your food1 : "))
user_foods2=(input("enter your food2 : "))
user_foods={"milk":1.02,"popcorn":2.5,"bread":2.5}
if (user_foods1=="milk" and user_foods2=="popcorn") or (user_foods2=="milk" and user_foods1=="popcorn"):
    print("your food price",user_foods["milk"]+user_foods["popcorn"])
elif (user_foods1=="milk" and user_foods2=="bread") or (user_foods2=="milk" and user_foods1=="bread"):
    print("your food price",user_foods["milk"]+user_foods["bread"])
elif (user_foods1=="popcorn" and user_foods2=="bread") or (user_foods2=="popcorn" and user_foods1=="bread"):
    print("your food price",user_foods["popcorn"]+user_foods["bread"])
else:
    print("sorry this food items not here")


"""user_foods1=(input("enter your food1 : "))
user_foods2=(input("enter your food2 : "))
user_foods3=(input("enter your food3 : "))
user_foods={"milk":1.02,"popcorn":2.5,"bread":2.5}
if (user_foods1=="milk"and user_foods2=="popcorn"and user_foods3=="bread")or(user_foods2=="milk"and user_foods3=="popcorn"and user_foods1=="bread")or (user_foods3=="milk"and user_foods1=="popcorn"and user_foods2=="bread"):
    print("your price is",user_foods["milk"]+user_foods["popcorn"]+user_foods["bread"])
else:
    print("your food is not here ")"""