def credit_card_balance():
    """ Calculates the remaining balance at the end of 12 months
    Input: balance, annual interest rate, monthly payment rate
    Output: remaining balance"""
    
    # outstanding balance on the credit card
    balance = int(input("What is your current balance? >> "))
    print(balance)

    # annual interest rate as a decimal
    annualInterestRate = float(input("What is the current annual interest rate? (i.e enter as 0.2 - 20%) >> "))
    print(annualInterestRate)

    # monthly payment rate
    monthlyPaymentRate = float(input("What is your monthly payment rate? (i.e enter as 0.04 - 4%) >> "))
    print(monthlyPaymentRate)

    # Montly interest rate = annual / 12.0
    monthlyInterestrate = annualInterestRate / 12.0
    print(monthlyInterestrate)


    for i in range(0,12):
   		# 2% minimum montly payment rate
    	minimumMonthlyPayment = monthlyPaymentRate * balance

    	# unpaid balance
    	unpaidBalance = balance - minimumMonthlyPayment

    	# updated balance
    	balance = unpaidBalance + (monthlyInterestrate * unpaidBalance)
    
    	print("Remaining balance: ", round(balance,2))

credit_card_balance()