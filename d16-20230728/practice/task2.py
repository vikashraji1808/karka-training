list1=[10,30,50,70,90,110]
list2=[15,35,55,65,95,100]
for each in range(len(list1)):
   if list1[each]>list2[each+1]:
      print(list1[each],"is the biggest number")
   elif list2[each+1]>list1[each]:
      print(list[each+1],"is the biggest number")
    