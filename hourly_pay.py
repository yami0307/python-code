hours=eval(input('Enter the no. of hours you\'ve worked in this week:'))
if hours<=37:
    pay=hours*23
elif hours<=65:
    b=hours-37
    pay=(37*23)+(b*31)
else:
    b=hours-65
    pay=(37*23)+(28*31)+(hours*41)
print('Your pay is', pay)
