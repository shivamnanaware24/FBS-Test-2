l = float(input("Enter wall length: "))
h = float(input("Enter wall height: "))
r = float(input("Enter rate per sq.m: "))

area = 4 * l * h
cost = area * r

print("Total Area of Four Walls: ", area)
print("Total Painting Cost: ", cost)