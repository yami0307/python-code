a,b,c=input("Enter the three sides of the triangle:").split()
a=eval(a);b=eval(b);c=eval(c)
if(a+b>c)or(b+c>a)or(a+c>b):
    if a==b==c:
        print("It is an equilateral triangle.")
    elif a==b or b==c or c==a:
        print("It is an isosceles triangle.")
    else:
        print("It is a scalene triangle.")
else:
    print("It is an invalid triangle")
    
