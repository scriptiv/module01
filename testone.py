#3.1
seconds_per_minute = 60
minutes_per_hour = 60
seconds_per_hour = seconds_per_minute * minutes_per_hour
print("Seconds per hour:", seconds_per_hour)

#3.2
seconds_in_minute = 60
minutes_in_hour = 60
seconds_in_hour = seconds_in_minute * minutes_in_hour
print("Seconds in hour:", seconds_in_hour)

#3.3
hours_in_day = 24
total_seconds_per_day = seconds_per_hour * hours_in_day
print("Total seconds per day:", total_seconds_per_day)

#3.4
seconds_per_day = total_seconds_per_day
print("Seconds per day:", seconds_per_day)

#3.5
floating_division_result = seconds_per_day / seconds_per_hour
print("Floating division result (seconds per day / seconds per hour):", floating_division_result)

#3.6
integer_division_result = seconds_per_day // seconds_per_hour
print("Integer division result (seconds per day // seconds per hour):", integer_division_result)