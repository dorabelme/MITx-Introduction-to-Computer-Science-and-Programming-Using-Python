def minimum_payment():
    """ Calculates the minimum payment needed to pay off credit card debt in 12 months
    Input: balance, annual interest rate
    Output: minimum monthly payment"""
    
    # outstanding balance on the credit card
    startingBalance = int(input("What is the starting balance? >> "))
    print(startingBalance)
    balance = startingBalance 
    numMonths = 12

    # annual interest rate as a decimal
    annualInterestRate = float(input("What is the current annual interest rate? (i.e enter as 0.2 - 20%) >> "))
    print(annualInterestRate)

    # Montly interest rate = annual / 12.0
    monthlyInterestrate = annualInterestRate / 12.0
    print(monthlyInterestrate)
    monthlyPayment = 10

    while balance > 0:
        balance = startingBalance       # reset the balance each iteration

        for i in range(0, numMonths):
            balance = balance - monthlyPayment 
            balance = balance + (monthlyInterestrate * balance)
        
        if balance > 0:
            monthlyPayment += 10

    
    print("Lowest payment: ", monthlyPayment)

minimum_payment()
