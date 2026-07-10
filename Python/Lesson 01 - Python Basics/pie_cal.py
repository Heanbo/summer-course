##pie calc
pi = float(3.1415926535)
pie_area = 0
print("CALCULATE PIE DIAMETER")
pie_diameter=int(input("enter the diameter of the larger pie "))
pie_area=pi * (pie_diameter / 2) ** 2
print(f"Pie Area is: {pie_area}")
print(pie_area)

#CALCULATE PIE COST
pie_cost = int(input("enter the cost of pie? "))
price_per_sq_inch =  pie_cost / pie_area
print(f"Price per square inch is: {price_per_sq_inch}")

#CALCULATE second pie
pie2_diameter=int(input("enter the diameter of the two second pies "))
pie2_area=pi * (pie2_diameter / 2) ** 2 * 2
print(f"Second Pie Area is: {pie2_area}")

#CALCULATE second pie cost
pie2_cost = int(input("enter the cost of second pie? "))
price_per_sq_inch2 =  pie2_cost / pie2_area
print(f"Price per square inch for second pie is: {price_per_sq_inch2}")

#Better Deal
if price_per_sq_inch < price_per_sq_inch2:
    print("The first pie is a better deal")
else:
    print("The second pie is a better deal")