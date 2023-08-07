"""fruits=["apple","orange","grapes"]
fruits.append("pinapple")    #add panurathuku
fruits.insert(0,"greeenapple")  #insertpanuradhu 
print(fruits)
# list
row1=["anish","anish","sam"]
row3=["vikash","chrish","ratheesh"]
two_rows=row1+row3
print(two_rows)"""
#distry
"""
details={"name":"vikash",
          "place":"peruvillai"
        }
details["phone"]="7548818374"
details["place"]="nagercoil"
print(details)
"""

friend_names=[{"name":"ratheesh","place":"perunthalaikadu","hobbies":["cricket","gym","vollyball"]},
               {"name":"vikash","place":"peruvillai","hobbies":["cricket","gym","kabbadi"]},
                {"name":"libin","place":"mamadivillai","hobbies":["biker riding","vollyball","running"]},
                {"name":"hari","place":"mondaymarket","hobbies":["kabbadi","cricket","vallyball"]},
                {"name":"azim","place":"thittuvillai","hobbies":["kabbadi","cricket","vallyball"]},
                {"name":"vinish","place":"boothapadi","hobbies":["pubg","thoroball","handball"]},
                {"name":"renitha","place":"thopur","hobbies":["watchingtv","game","gardening"]},
                {"name":"delma","place":"midalam","hobbies":["gardening","drawing","chess"]}]
#friend_names.append({"name":"chrish","place":"krishnakovil","hobby":["cricket","game","goingoutside"]})

# for fri in friend_names:
#   fri["hobby"].append("codding")
# print(friend_names)


for f in friend_names:
  for hobby in f["hobbies"]:
    print(hobby)



