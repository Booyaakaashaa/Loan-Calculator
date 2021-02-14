"""loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

# write your code here
print(loan_principal + "\n" + first_month + "\n" + second_month + "\n" + third_month + "\n" + final_output)
"""
loan_principal = int(input("Enter the loan principal:\n"))
choice = input("What do you want to calculate?\ntype \"m\" - for number of monthly payments,\ntype \"p\" - for the monthly payment:\n")
if choice == "m":
    monthly_payment = int(input("Enter the monthly payment:\n"))
    print("It will take {} months to replay the loan".format(loan_principal // monthly_payment))
elif choice == "p":
    no_of_months = int(input("Enter the number of months:\n"))

