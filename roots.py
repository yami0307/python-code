import math
a,b,c=input('Enter the three co-efficients of the quadratic equation').split()
a=eval(a);b=eval(b);c=eval(c)
d=(b**2)-(4*a*c)
D=math.sqrt(d)
r1=(-b+D)/(2*a)
r2=(-b-D)/(2*a)
print('The two roots of the equation are:', r1,'and', r2)
