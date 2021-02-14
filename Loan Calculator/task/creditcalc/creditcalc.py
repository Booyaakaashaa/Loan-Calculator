from math import ceil, log, pow
import sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["annuity", "diff"], help="Incorrect parameters")
parser.add_argument("--principal", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=int)
parser.add_argument("--periods", type=int)
args = parser.parse_args()

"""principal = int(args.principal)
interest = float(args.interest)
periods = int(args.periods)
payment = int(args.payment)"""

if args.type == "diff" and args.principal and args.interest and args.periods and args.nums == 4:
    if args.payment or args.principal < 0 or args.interest < 0 or args.periods < 0:
        print("Incorrect parameters")
    else:
        i = 1
elif args.type == "annuity" and args.nums == 4:
    if not args.periods:
        i = args.interest / 12 / 100
        n = args.payment / (args.payment - i * args.principal)
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
    elif not args.principal:
        i = args.interest / 12 / 100
        x = pow(i + 1, args.periods)
        principal = (x - 1) * args.payment / x / i
        print("Your loan principal = {}!".format(round(principal)))
    elif not args.payment:
        i = args.interst / 12 / 100
        x = pow(i + 1, args.periods)
        payment = ceil(args.principal * i * x / (x - 1))
        print("Your monthly payment = {}!".format(round(payment)))
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")

"""from math import ceil, log, pow
import sys

# choice = input(What do you want to calculate?
# type "n" for number of monthly payments,
# type "a" for annuity monthly payment amount,
# type "p" for loan principal:\n)

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
    print("Your loan principal = {}!".format(round(principal)))"""
