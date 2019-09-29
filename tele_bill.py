call=eval(input("Enter the number of calls"))
if call<=75:
    charge=75
elif call<=150:
    b=call-75
    charge=75+(b*.75)
elif call<=240:
    b=call-150
    charge=75+(75*.75)+(b*.65)
else:
    b=call-240
    charge=75+(75*.75)+(90*.65)+(b*.55)
print('The monthly bill of the telephone company is:', charge)
