year=input("Enter any year")
y_l=len(year)
if y_l==4:
    if 1900<int(year)<2019:
        print("The entered year is valid year")
    else:
        print("It is an invalid year")

else:
    print("It is an invalid year")
