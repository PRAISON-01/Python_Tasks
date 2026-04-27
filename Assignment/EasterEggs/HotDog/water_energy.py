"""
water_energy.py

collect amt_of_water
collect initial_temp
collect final_temp
energy_needed = (amt_of_water) * (final_temp - inital_temp) * 4184
print energy_needed
"""
amt_of_water = int(input("Enter water in kilograms: "))
final_temp = int(input("Enter final Temperature: "))
initial_temp = int(input("ENter initiual Temperature: "))
energy_needed = (amt_of_water) * (final_temp - initial_temp) * 4184
print(f"Energy needed is {energy_needed}")
