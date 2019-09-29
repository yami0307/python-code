prr=eval(input("Enter the previous reading: "))
crr=eval(input("Enter the current reading: "))
if prr>crr:
    unit=(10000000+prr)-crr
else:
    unit=crr-prr
if unit<=25:
    charge=unit*4.89
elif unit<=60:
    b=unit-25
    charge=(25*4.89)+(b*5.45)
elif unit<=84:
    b=unit-60
    charge=(25*4.89)+(35*5.45)+(b*6.41)
else:
    b=unit-84
    charge=(25*4.89)+(35*5.45)+(24*6.41)+(b*9.95)
print('Your monthly electriity bill is', (charge+15))

        
