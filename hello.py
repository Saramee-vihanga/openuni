Name=input("Enter your name: ")
SID=int(input("Enter your SID: "))
print("Hello " + Name + " welcome to the selection test ")
MARKS=int(input("Enter your CAT 1 marks: "))

if(MARKS>=75):
    print("Grade=A")
elif(MARKS>=65):
    print("Grade=B")
elif(MARKS>=55):
    print("Grade=C")
else:
    print("S")