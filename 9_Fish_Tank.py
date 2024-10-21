length = int(input())
width = int(input())
height = int(input())  #всичко в СМ
percentage_used = float(input())

water_in_cm = length * width * height #в СМ 3
water_in_m = water_in_cm * 0.001
percentage_used_in_m = percentage_used / 100

needed_water = water_in_m * (1 - percentage_used_in_m)
print(needed_water)
