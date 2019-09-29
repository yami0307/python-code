n=int(input("Enter the year number of your wish"))
boo= 'It is a leap year' if ((n%400==0) or((n%4==0) and (n%100!=0))) else 'It is not a leap year'
print(boo)
