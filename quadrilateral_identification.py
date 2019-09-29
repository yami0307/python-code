a,b,c,d=input("Enter the 4 sides of the quadrilateral: ").split()
A=eval(input("Enter one interior angle of the quadrilateral: "))
if a==b==c==d and A==90:
    print("The quadrlateral is a square.")
elif a==b==c==d and A!=90:
    print("The quadrilateral is a rhombus.")
elif a==c and b==d and A!=90:
    print("The quadrilateral is a parallelogram.")
elif a==c and b==d and A==90:
    print("The quadrilateral is a rectangle.")
else:
    print("It is an irregular shaped quadrilateral.")
