n=int(input("Enter the number of human years:"))
if n < 0:
  print("Human years cannot be negative.")
elif n<=2:
  print(n,"human years is equivalent to",n*10.5)
elif n>=3:
 print(n,"human years is equivalent to",21+(n-2)*4)