"""friend_names=["ratheesh","vikash","libin","hari","azim","vinish","renitha","delma"]
print(friend_names[0:3])

my_details={"name":"vikash","place":"peruvillai"}
# iam taking only place
print(my_details["name"])

friend_names=[{"name":"ratheesh","place":"perunthalaikadu"},
               {"name":"vikash","place":"peruvillai"},
                {"name":"libin","place":"mamadivillai"},
                {"name":"hari","place":"mondaymarket"},
                {"name":"azim","place":"thittuvillai"},
                {"name":"vinish","place":"boothapadi"},
                {"name":"renitha","place":"thopur"},
                {"name":"delma","place":"midalam"}]
print(friend_names[0])
print(friend_names[5])

friend_names=[{"name":"ratheesh","place":"perunthalaikadu","hobby":["cricket","gym","vollyball"]},
               {"name":"vikash","place":"peruvillai","hobby":["cricket","gym","kabbadi"]},
                {"name":"libin","place":"mamadivillai","hobby":["biker ridding","vollyball","running"]},
                {"name":"hari","place":"mondaymarket","hobby":["kabbadi","cricket","vallyball"]},
                {"name":"azim","place":"thittuvillai","hobby":["kabbadi","cricket","vallyball"]},
                {"name":"vinish","place":"boothapadi","hobby":["pubg","thoroball","handball"]},
                {"name":"renitha","place":"thopur","hobby":["watchingtv","game","gradening"]},
                {"name":"delma","place":"midalam","hobby":["gradaning","drawing","chess"]}]
print(friend_names) """              

# friend_names=[{"name":"ratheesh","place":"perunthalaikadu","hobby":["cricket","gym","vollyball"]},
#                {"name":"vikash","place":"peruvillai","hobby":["cricket","gym","kabbadi"]},
#                 {"name":"libin","place":"mamadivillai","hobby":["biker ridding","vollyball","running"]},
#                 {"name":"hari","place":"mondaymarket","hobby":["kabbadi","cricket","vallyball"]},
#                 {"name":"azim","place":"thittuvillai","hobby":["kabbadi","cricket","vallyball"]},
#                 {"name":"vinish","place":"boothapadi","hobby":["pubg","thoroball","handball"]},
#                 {"name":"renitha","place":"thopur","hobby":["watchingtv","game","gradening"]},
#                 {"name":"delma","place":"midalam","hobby":["gradaning","drawing","chess"]}]
# print(friend_names[0]["hobby"][0])                

friend_names=[{"name":"ratheesh","place":"perunthalaikadu","hobby":["cricket","gym","vollyball"],"subject":{"tamil=90","english=36"}},
               {"name":"vikash","place":"peruvillai","hobby":["cricket","gym","kabbadi"]},
                {"name":"libin","place":"mamadivillai","hobby":["biker riding","vollyball","running"]},
                {"name":"hari","place":"mondaymarket","hobby":["kabbadi","cricket","vallyball"]},
                {"name":"azim","place":"thittuvillai","hobby":["kabbadi","cricket","vallyball"]},
                {"name":"vinish","place":"boothapadi","hobby":["pubg","thoroball","handball"]},
                {"name":"renitha","place":"thopur","hobby":["watchingtv","game","gardening"]},
                {"name":"delma","place":"midalam","hobby":["gardening","drawing","chess"]}]
print(friend_names[0]["subject"])               