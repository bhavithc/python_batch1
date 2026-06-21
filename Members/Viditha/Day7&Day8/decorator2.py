def profit(i):

    print(f"profit amount {i}")

def loss(j):
    print(f"Loss amount {j}")

def calculate_profit_loss(c,sold):
    prod_cost=int(input("Enter the product cost"))
    diff=int(sold)-prod_cost
    if prod_cost<sold:
        c(diff)
    else:
        loss(diff)    

sold=int(input("Enter the sold cost"))
calculate_profit_loss(profit,sold)


        