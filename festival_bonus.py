basic_pay=eval(input('Enter your basic pay: '))
desig=input('Enter your designation:')
if desig=='manager' or desig=='Manager':
    if basic_pay<40000:
        bonus=basic_pay*.12
        if bonus<2500:
            bonus=2500
    else:
        bonus=basic_pay*.16
        if bonus>7500:
            bonus=7500
elif desig=='officer' or desig=='Officer':
    if basic_pay<20000:
        bonus=basic_pay*.14
        if bonus<2500:
            bonus=2500
        elif bonus>5000:
            bonus=5000
    else:
        bonus=basic_pay*.089
else:
    bonus=basic_pay*.089
print(bonus,' is your festival bonus.')
