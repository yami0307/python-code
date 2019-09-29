A,B,C=input("Enter the three angles of the triangle").split()
A=eval(A);B=eval(B);C=eval(C)
S=A+B+C
if S!=180:
    print("The triangle is an invalid one.")
else:
    if A==B==C:
        print("It is an equiangular triangle.")
    elif A==90 or B==90 or C==90:
        print("It is a right-angled triangle.")
    elif A<90 and B<90 and C<90:
        print("It is an acute angled triangle.")
    elif A>90 or B>90 or C>90:
        print("It is an obtuse angled triangle.")
