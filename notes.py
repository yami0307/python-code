amt=eval(input("Enter an amount: "))
lis=[2000,500,200,100]
notes=[]
for i in range(0,4):
    b=amt//lis[i]
    amt=amt%lis[i]
    notes.append(b)
print(notes)

'''while amt>0:
    b=amt/lis[0]
if amt>2000:
    c=amt/2000
    b=amt%2000
    if b>500:
        c1=b/500
        b1=b%500
        if b1>200:
            c2=b1/200
            b2=b1%200'''
