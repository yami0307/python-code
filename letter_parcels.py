weight=eval(input('Enter the weight of the letter parcels in grams:'))
if weight<=375:
    g=weight-10
    h=g/11
    charge=23+(h*17.75)
    if weight>375:
        j=weight-375
        charge=23+(h*17.75)+(j*1.75)

print('The registration charge of letter parcels is ',charge)
