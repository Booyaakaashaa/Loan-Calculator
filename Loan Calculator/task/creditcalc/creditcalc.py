from math import ceil, log, pow, floor
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["annuity", "diff"], type=str)
parser.add_argument("--principal", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=int)
parser.add_argument("--periods", type=int)
args = parser.parse_args()
# print([args.type, args.principal, args.interest, args.payment, len(sys.argv)])
if args.type == "diff" and args.principal and args.interest and args.periods and len(sys.argv) == 5:
    if args.payment or args.principal < 0 or args.interest < 0 or args.periods < 0:
        print("Incorrect parameters")
    else:
        total = 0
        i = args.interest / 100 / 12
        P = args.principal
        n = args.periods
        for x in range(1, args.periods + 1):
            D = P / n + i * (P - (P * (x - 1)) / n)
            print("Month {}: payment is {}".format(x, ceil(D)))
            total += ceil(D)
        print("\nOverpayment = {}".format(total - args.principal))
elif args.type == "annuity" and len(sys.argv) == 5:
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
        print("Overpayment = {}".format(args.payment * time - args.principal))
    elif not args.principal:
        i = args.interest / 12 / 100
        x = pow(i + 1, args.periods)
        principal = (x - 1) * args.payment / x / i
        print("Your loan principal = {}!".format(floor(principal)))
        print("Overpayment = {}".format(args.payment * args.periods - floor(principal)))
    elif not args.payment:
        i = args.interest / 12 / 100
        x = pow(i + 1, args.periods)
        payment = ceil(args.principal * i * x / (x - 1))
        print("Your annuity payment = {}!".format(round(payment)))
        print("Overpayment = {}".format(round(payment) * args.periods - args.principal))
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
