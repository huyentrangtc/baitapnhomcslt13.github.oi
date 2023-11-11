#nhap gia tri
denomination = int(input("Enter the denomination of the banknote: "))
#phan tich gia tri
if denomination == 1:
    print("The individual on the $1 banknote is George Washington.")
elif denomination == 2:
    print("The individual on the $2 banknote is Thomas Jefferson.")
elif denomination == 5:
    print("The individual on the $5 banknote is Abraham Lincoln.")
elif denomination == 10:
    print("The individual on the $10 banknote is Alexander Hamilton.")
elif denomination == 20:
    print("The individual on the $20 banknote is Andrew Jackson.")
elif denomination == 50:
    print("The individual on the $50 banknote is Ulysses S. Grant.")
elif denomination == 100:
    print("The individual on the $100 banknote is Benjamin Franklin.")
else:
    print("No such banknote exists.")