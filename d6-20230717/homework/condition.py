"""token_num=int(input("enter token_num : "))
if token_num>500 and token_num<1000:
    print("you have owned a silver token")
elif token_num>=1000 and token_num<5000:
    print("you have owned a golden token")
elif token_num>=5000:
    print("you have owned a platinum token")
else:
    print("no token availabl")"""

email=input("enter your emai  : ")
password=input("enter your password : ")
if email=="vikash@gmail.com" and password=="v1234567":
    print("login sucessfully")
elif email=="vikash@gmail.com" or password=="v123333":
    print("wrong password please check your password")
elif email=="vikas@gmail.com" or password=="v1234567":
    print("wrong email please check your email")
else:
    print("you are not authenticated")       
