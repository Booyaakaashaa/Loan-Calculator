
from math import ceil, log

loan_principal = int(input("Enter the loan principal:\n"))
choice = input("What do you want to calculate?\ntype \"m\" - for number of monthly payments,\ntype \"p\" - for the monthly payment:\n")
if choice == "m":
    monthly_payment = int(input("Enter the monthly payment:\n"))
    print()
    period = ceil(loan_principal / monthly_payment)
    if period == 1:
        print("It will take {} month to replay the loan".format(ceil(loan_principal / monthly_payment)))
    else:
        print("It will take {} months to replay the loan".format(ceil(loan_principal / monthly_payment)))
elif choice == "p":
    no_of_months = int(input("Enter the number of months:\n"))
    if loan_principal // no_of_months == ceil(loan_principal / no_of_months):
        print()
        print("Your monthly payment = {}".format(loan_principal // no_of_months))
    else:
        print()
        payment = ceil(loan_principal / no_of_months)
        last_payment = loan_principal - (no_of_months - 1) * payment
        print("Your monthly payment = {} and the last payment = {}".format(payment, last_payment))
