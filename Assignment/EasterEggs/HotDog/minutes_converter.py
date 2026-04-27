"""
minutes_converter.py

collect input total_minutes
years = total_minutes // 52560
rem_years = total_minutes % 52560
day = total_minutes // 1440
rem_min = rem_years % 10
print  
"""
total_minutes = int(input("Enter tptal minutes: "))
years = total_minutes // 525600
rem_years = total_minutes % 52560
day = rem_years // 1440
rem_min = rem_years % 1440
print(f" {total_minutes} minutes is {years} years,{day} days, {rem_min} minutes")
