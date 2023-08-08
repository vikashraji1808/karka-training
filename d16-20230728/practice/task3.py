# n=5
# for i in range(n):
#     for j in range(n):
#         print("$",end="")
#     print ()

n=int(input("enter the number :"))
for i in range(1,(n*n)+1):
    print((n*n)+1-i,end="")
    if i%n==0:
        print("\n")
n=int(input("enter the number :"))
for i in range(n):
    for j in range(n):
    print((n*n)+1-i,end="")
    if i%n==0:
        print("\n")

    

     
