print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
if x == y == z:
    print("that is Equilateral triangle")
elif x==y or y==z or z==x:
    print("that is isosceles triangle")
else:
    print("that is Scalene triangle")