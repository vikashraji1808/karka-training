students_data = [
    {
        "name": "John",
        "mid_term_result" : {"math": 30, "science": 42},
        "attendance": [
            {"month": "july", "total_working_days": 26, "leave": 3},
            {"month": "augest", "total_working_days": 24, "leave": 0},
            {"month": "sept", "total_working_days": 25, "leave": 2}
        ]
    },
    {
        "name": "Emma",
        "mid_term_result": {"math": 20, "science": 49},
        "attendance": [
            {"month": "july", "total_working_days": 26, "leave": 6},
            {"month": "augest", "total_working_days": 24, "leave": 10},
            {"month": "sept", "total_working_days": 24, "leave": 5}
        ]
    },
    {
        "name": "Alex",
        "mid_term_result": {"math": 30, "science": 40},
        "attendance": [
            {"month": "july", "total_working_days": 26, "leave": 5},
            {"month": "augest", "total_working_days": 24, "leave": 6},
            {"month": "sept", "total_working_days": 24, "leave": 4}
        ]
    },
]


print("Students not eligible for the quarterly exam:")
for student in students_data:

    math_score = student["mid_term_result"]["math"]
    science_score = student["mid_term_result"]["science"]

    total_working_days = 0
    total_leaves = 0

    for attendance_data in student["attendance"]:
        total_working_days += attendance_data["total_working_days"]
        total_leaves += attendance_data["leave"]

    attendance_percentage = ( (total_working_days - total_leaves) / total_working_days ) * 100

    if (math_score < 35 or science_score < 35) and attendance_percentage < 80:
        print(student["name"])

#This task will explain to analyses the data to find the month with min and max gold rate along with the total cost of each jewel for the months with the min and max god rates.
"""
monthly_jwel_rate = [
    {"month":"Jan",
     "gold_rate":2000,
     "jwels_list":[{
         "name":"chain",
         "making_charge":12
     },{
         "name":"ring",
         "making_charge":10
     }]},
     {"month":"Feb",
     "gold_rate":4000,
     "jwels_list":[{
         "name":"chain",
         "making_charge":12
     },{
         "name":"ring",
         "making_charge":10
     }]},
     {"month":"March",
     "gold_rate":3600,
     "jwels_list":[{
         "name":"chain",
         "making_charge":12
     },{
         "name":"ring",
         "making_charge":10
     }]},
     {"month":"April",
     "gold_rate":3678,
     "jwels_list":[{
         "name":"chain",
         "making_charge":12
     },{
         "name":"ring",
         "making_charge":10
     }]},
     {"month":"May",
     "gold_rate":4500,
     "jwels_list":[{
         "name":"chain",
         "making_charge":12
     },{
         "name":"ring",
         "making_charge":10
     }]},
]
 
min_rate = monthly_jwel_rate[0]["gold_rate"]
max_rate = 0
min_max_data  = {}
for jwel_data in monthly_jwel_rate:
    gold_rate = jwel_data["gold_rate"]
    month = jwel_data['month']
    if gold_rate <= min_rate:
        min_rate = gold_rate
        min_rate_month = month

    if gold_rate >= max_rate:
        max_rate = gold_rate
        max_rate_month = month

min_max_data['min_month_rate'] = {
    "month":min_rate_month,
    "gold_rate":min_rate,
    }
min_max_data['max_month_rate'] = {
    "month":max_rate_month,
    "gold_rate":max_rate}


for jwels_data in monthly_jwel_rate:

    jwels_list = jwels_data["jwels_list"]
    gold_rate = jwels_data["gold_rate"]
    month = jwels_data['month']
    for jwels in jwels_list:
        making_charge = gold_rate *(jwels["making_charge"]/100)
        gst = gold_rate * .18
        total = gold_rate + making_charge + gst
        if month == min_rate_month:
            min_max_data['min_month_rate'][jwels['name']] = total
        elif month == max_rate_month:
            min_max_data['max_month_rate'][jwels['name']] = total
            

print(min_max_data)"""

#This task to help you determine how many units of a specific item you can purchase within your budget. Additionally, the program should display the total cost of the selected item and any remaining amount after the purchase.      

"""
grocery_items = [
    {"item": "Apples", "price": 2.50},
    {"item": "Bananas", "price": 1.70},
    {"item": "Milk", "price": 3.20},
    {"item": "Bread", "price": 2.00},
    {"item": "Eggs", "price": 2.80},
    {"item": "Cheese", "price": 5.50},
    {"item": "Tomatoes", "price": 1.90},
    {"item": "Potatoes", "price": 2.10},
    {"item": "Onions", "price": 1.50},
    {"item": "Chicken", "price": 8.00}
]

budget_limit = int(input("Enter the amount you have "))
selected_item = input("Which Item You Want to buy ")
item_rate=0
bool_value=False
for item in grocery_items:
    if item["item"]==selected_item:
        bool_value=True
        item_rate=item["price"]
if bool_value:   
    max_quantity = budget_limit / item_rate
    remaining_cost = budget_limit % item_rate 
    total_cost = item_rate * max_quantity
      
    if max_quantity > 0:
        print(selected_item, max_quantity,"units - Total Cost: $",total_cost)
        if remaining_cost>0:
            print("Remaining Amount You Have",remaining_cost)
            
    else: 
        print("Sorry You Didn't have enough amount to buy an item")
else:
    print("no item")
 """   




