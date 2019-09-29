#profit or loss on a sale
cost=eval(input("Enter the buying price of the product: "))
price=eval(input("Enter the selling price of the product:"))
diff=price-cost
if diff>0:
    print("The profit is of", diff)
else:
    print("The loss is of", -diff)
