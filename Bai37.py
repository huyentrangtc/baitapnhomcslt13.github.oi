side=int(input("Enter sides of shape to determine its name:"))
if side == 3:
        side = "Triangle"
elif side == 4:
        side = "Quadrilateral"
elif side == 5:
        side = "Pentagon"
elif side == 6:
        side = "Hexagon"
elif side == 7:
        side = "Heptagon"
elif side == 8:
        side = "Octagon"
elif side == 9:
        side = "Nonagon"
elif side == 10:
        side = "Decagon"
else:
      print("error")
print(side)