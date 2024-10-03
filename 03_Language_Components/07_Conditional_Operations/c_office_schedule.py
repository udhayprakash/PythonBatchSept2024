#!/usr/bin/python3
"""
Purpose: Office Schedule
    Monday to Friday  :- 9 am CDT to 5 pm CDT
    Saturday          :- 9 am CDT to 1 pm CDT
    Sunday            :- Holiday

    In runtime, user will give week name, and 
    they should be that day schedule
"""

# week_of_day = "Monday"
week_of_day = input("Enter week of the day:").strip().title()

#  Method 1
# if week_of_day == "Monday":
#     print("TIMINGS: 9 AM to 6 PM")
# elif week_of_day == "Tuesday":
#     print("TIMINGS: 9 AM to 6 PM")
# elif week_of_day == "Wednesday":
#     print("TIMINGS: 9 AM to 6 PM")
# elif week_of_day == "Thursday":
#     print("TIMINGS: 9 AM to 6 PM")
# elif week_of_day == "Friday":
#     print("TIMINGS: 9 AM to 6 PM")
# elif week_of_day == "Saturday": # or week_of_day == "saturday":
#     print("TIMINGS: 9 AM to 1 PM")
# elif week_of_day == "Sunday":
#     print("----HOLIDAY----------")
# else:
#     print("INVALID ENTRY! PLEASE TRY AGAIN!!")


# Method 2
# WEEKDAY_TIMINGS = "TIMINGS: 9 AM to 6 PM"
# if week_of_day == "Monday":
#     print(WEEKDAY_TIMINGS)
# elif week_of_day == "Tuesday":
#     print(WEEKDAY_TIMINGS)
# elif week_of_day == "Wednesday":
#     print(WEEKDAY_TIMINGS)
# elif week_of_day == "Thursday":
#     print(WEEKDAY_TIMINGS)
# elif week_of_day == "Friday":
#     print(WEEKDAY_TIMINGS)
# elif week_of_day == "Saturday": # or week_of_day == "saturday":
#     print("TIMINGS: 9 AM to 1 PM")
# elif week_of_day == "Sunday":
#     print("----HOLIDAY----------")
# else:
#     print("INVALID ENTRY! PLEASE TRY AGAIN!!")


# Method 3
# WEEKDAY_TIMINGS = "TIMINGS: 9 AM to 6 PM"
# if (
#     week_of_day == "Monday" or  
#     week_of_day == "Tuesday" or 
#     week_of_day == "Wednesday" or  
#     week_of_day == "Thursday" or  
#     week_of_day == "Friday"
#     ):
#     print(WEEKDAY_TIMINGS)
# elif week_of_day == "Saturday": # or week_of_day == "saturday":
#     print("TIMINGS: 9 AM to 1 PM")
# elif week_of_day == "Sunday":
#     print("----HOLIDAY----------")
# else:
#     print("INVALID ENTRY! PLEASE TRY AGAIN!!")


# Method 4 -  MEMBERSHIP CHECK
WEEKDAY_TIMINGS = "TIMINGS: 9 AM to 6 PM"
if  week_of_day in ("Monday" , "Tuesday" , "Wednesday", "Thursday" or  
    week_of_day == "Friday"
    ):
    print(WEEKDAY_TIMINGS)
elif week_of_day == "Saturday": # or week_of_day == "saturday":
    print("TIMINGS: 9 AM to 1 PM")
elif week_of_day == "Sunday":
    print("----HOLIDAY----------")
else:
    print("INVALID ENTRY! PLEASE TRY AGAIN!!")
