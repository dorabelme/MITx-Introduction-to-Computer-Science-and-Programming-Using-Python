def minimum_payment_bounds():
    """ Calculates the minimum payment needed to pay off credit card debt in 12 months
    Input: balance, annual interest rate
    Output: minimum monthly payment"""
    
    # outstanding balance on the credit card
    startingBalance = int(input("What is the starting balance? >> "))
    print(startingBalance)
    numMonths = 12

    # annual interest rate as a decimal
    annualInterestRate = float(input("What is the current annual interest rate? (i.e enter as 0.2 - 20%) >> "))
    print(annualInterestRate)
    monthlyInterestrate = annualInterestRate / 12
    print(monthlyInterestrate)
    epsilon = 0.01

    # bounds
    lower_bound = startingBalance / 12.0
    upper_bound = (startingBalance * (1 + monthlyInterestrate) ** 12) / 12.0
    
    balance = startingBalance

    while abs(balance) > epsilon:
        print(lower_bound, upper_bound)

        monthlyPayment = (upper_bound + lower_bound) / 2.0
        balance = startingBalance
        
        for i in range(12):
            balance = balance - monthlyPayment + ((balance - monthlyPayment) * monthlyInterestrate)

        if balance > epsilon:
            lower_bound = monthlyPayment
        elif balance < -epsilon:
            upper_bound = monthlyPayment
        else:
            break

    print("Lowest payment: ", round(monthlyPayment,2))

minimum_payment_bounds()