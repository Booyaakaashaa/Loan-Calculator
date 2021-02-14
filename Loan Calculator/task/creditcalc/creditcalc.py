from math import ceil, log, pow

choice = input("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:\n""")

if choice == "n":
    principal = int(input("Enter the loan principal:\n"))
    payment = int(input("Enter the monthly payment:\n"))
    i = float(input("Enter the loan interest:\n")) / 12 / 100
    n = payment / (payment - i * principal)
    time = ceil(log(n, i + 1))
    years, months = time // 12, time % 12
    if years == 0:
        if months == 1:
            print("It will take 1 month to repay this loan!")
        else:
            print("It will take {} months to repay this loan!".format(months))
    elif months == 0:
        if years == 1:
            print("It will take 1 year to repay this loan!")
        else:
            print("It will take {} years to repay this loan!".format(years))
    else:
        if years == 1 and months == 1:
            print("It will take 1 year and 1 month to repay this loan!")
        elif months == 1:
            print("It will take {} years and 1 month to repay this loan!".format(years))
        elif years == 1:
            print("It will take 1 year and {} months to repay this loan!".format(months))
        else:
            print("It will take {} years and {} months to repay this loan!".format(years, months))
elif choice == "a":
    principal = int(input("Enter the loan principal:\n"))
    period = int(input("Enter the number of periods:\n"))
    i = float(input("Enter the loan interest:\n")) / 12 / 100
    x = pow(i + 1, period)
    payment = ceil(principal * i * x / (x - 1))
    print("Your monthly payment = {}!".format(round(payment)))
elif choice == "p":
    payment = float(input("Enter the annuity payment:\n"))
    period = int(input("Enter the number of periods:\n"))
    i = float(input("Enter the loan interest:\n")) / 12 / 100
    x = pow(i + 1, period)
    principal = (x - 1) * payment / x / i
    print("Your loan principal = {}!".format(round(principal)))
