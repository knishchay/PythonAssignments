def wallet(initial):
    balance=initial
    def deposit(cash):
        nonlocal balance
        balance+=cash
        print('deposited money is:',balance)
    
    
    def spending(cash):
        nonlocal balance
        if(balance<cash):
            print("Insufficient balance")
        else:
            balance=balance-cash
        print('money spent is', cash)
    
    def savings():
        nonlocal balance
        print('money left is', balance)
     


    def transfer(wal, amount):
        nonlocal balance
        if amount <= balance:
            balance = balance - amount
            var1 = wal
            var1["deposit"](amount)
            print("Deducted Amount" + str(amount) + " Balance: "+str(balance))

    out = {"deposit": deposit, "spending": spending, "savings": savings, "transfer": transfer }
    
    return out


out1 = wallet(5000)
out2 = wallet(600)

out1["transfer"](wallet(300), 800)
out1["savings"]()
out1["deposit"](900)
out1["spending"](190)
out1["savings"]()




