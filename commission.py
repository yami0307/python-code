salea=eval(input("Enter the amount of sales in region A"))
saleb=eval(input("Enter the amount of sales in region B"))
tsale=salea+saleb
if salea<10000:
    commission=0
elif salea<16000 and saleb<15000:
    commission=tsale*.065
elif salea<35000 and saleb<25000:
    commission=(tsale*.085)+1500
else:
    commission=(tsale*.11)+4500
print('The commission is ', commission)
