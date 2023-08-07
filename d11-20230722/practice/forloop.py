"""numbers=[9,10,12,13,14,15,16,25,30]
for number in numbers:
    if number%3==0 and number%5==0:
        print("fizzbuzz")
    elif number%3==0:
        print("fizz")
    elif number%5==0:
        print("buzz")
    else:
        print(number)
"""

"""monthly_gold_rate=[{"month":"jan","gold_rate":1000,"jewls":[{"name":"chain","making_chrge":10}
                                                             {"nmae":"ring","making_chrge":12}
                                                             {"name":"brace","making_chrge":9}]},
                    {"month":"feb","gold_rate":2000,"jewls":[{"name":"chain","making_chrge":14}
                                                              {"nmae":"ring","making_chrge"6}
                                                              {"nmae":"brace","making_chrge":12}]},
                    {"month":"mar","gold_rate":3000,"jewls":[{"name":"chain","making_chrge":15}
                                                              {"nmae":"ring","making_chrge":17}
                                                              {"nmae":"brace","making_chrge":22}]},
                    {"month":"aprl","gold_rate":9000,"jewls":[{"name":"chain","making_chrge":19}
                                                              {"nmae":"ring","making_chrge":.10}
                                                              {"nmae":"brace","making_chrge":23}]}]"""
"""goldrate1=monthly_gold_rate[0]["gold_rate"]
goldrate2=0
minmonth=monthly_gold_rate[0]["month"]
maxmonth=monthly_gold_rate[0]["month"]

for a in monthly_gold_rate:
    if a["gold_rate"]<goldrate1:
        goldrate1=a["gold_rate"]
        minmonth=a["month"]
    elif a["gold_rate"]>goldrate2:
        goldrate2=a["gold_rate"]
        maxmonth=a["month"]

print("the gold price is lower in :",minmonth,goldrate1)
print("the gold price is higher in:",maxmonth,goldrate2)"""

"""user_details=[
              {
                "name":"ajay",
                "marks":[80,90,70,40,60]
              }
              {
                "name":"manimala",
                "marks":[100,80,40,90,70] 
              }
              ]
for student in user_details:
    print(student)"""


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


