# the number of even and odd number 
number=[1,2,3,4,5,6,7,8,9]
even=0
odd=0
for num in number:
    if num%2==0:
        even=even+1
    else:
        odd=odd+1
print("number of even number : ",even)
print("number of odd number : ",odd)
#the real number in this mixed list
"""mixedlist=[1,2.0,"hai","@",5,6,"&",8,9]
count=0
for mixed in mixedlist:
    if type(mixed)==int:
        count=count+1
print("number in a mixedlist : ",count)"""

# mixedlist=[1,2.0,"hai","@",5,6,"&",8,9]
# count=0
# for mixed in mixedlist:
#     if type(mixed)==float:
#         count=count+1
# print("number in a mixedlist : ",count)

    

    
