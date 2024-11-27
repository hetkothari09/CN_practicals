no=int(input("Enter the number of Frames:"))
z=""
for i in range(no):
    x=input(f"Enter {i+1} frame:")
    y=len(x)+1
    z=z+str(y)+x
print(z)
