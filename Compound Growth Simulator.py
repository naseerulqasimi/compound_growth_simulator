print("welcome dear!".title())
print("\ncumulative annual growth rate calculator".upper())
print("by muhammad naseer".title())
print("--------------------\n")
# 1) Get the input values and convert the string into int or float where required

principal = float(input("Please insert the principal amount (Rs.) = "))
inflation = float(input("Please insert the expected inflation value % = "))
inflation = inflation/100
growth_rate = float(input("Please insert the expected (optimistic) growth rate % = "))
con_growth_rate = float(input("Please enter your a conservative growth rate % = "))
growth_rate = growth_rate/100
con_growth_rate = con_growth_rate/100
annual = float(input("Please insert the annual contribution (Rs.) = "))
years = int(input("Please insert the number of years for investment = "))
target=float(input("What is your target to achieve? Enter Amount Rs. = "))
balance = principal
con_balance = principal
t_annual=0

# 2) Use a for loop and range() function to go through the years

for year in range(1,years + 1):
    print(f"---Year {year}---")
    balance = balance * (1 + growth_rate)
    balance = balance + annual
    con_balance = con_balance * (1 + con_growth_rate)
    con_balance = con_balance + annual
    t_annual=t_annual+annual
    print(f"Your Balance for the year is Rs. {balance:.2f}.")
    print(F"Your Balance for the Year based on Conservative Growth rate is Rs. {con_balance:.2f}.")
    if balance >= principal * 2:
        print("Your principal amount is doubled.")
    if con_balance >= principal * 2:
        print("Your principal amount is also doubled based on conservative growth rate.")
    real = balance / (1 + inflation) ** year
    con_real = con_balance / (1 + inflation) ** year
    print(f"Your Real Growth is Rs. {real:.2f}.")
    print(f"Your Real Growth based on conservative growth rate is Rs. {con_real:.2f}.")

# 3) Get the CAGR and total amount invested

cagr = (balance / principal) ** (1/years) -1
con_cagr = (con_balance / principal) ** (1/years) -1
total = t_annual+principal

print(f"Your Cumulative Annual Growth Rate of the principal amount (CAGR) is {cagr*100:.2f}%.")
#summary
print("---Summary---".upper())
print("__________________________________________________________")

#Optimistic Calculation

print("***Optimistic Calculation***".upper())
print(f"FINAL AMOUNT {balance:.2f}"
      f"\nTOTAL AMOUNT INVESTED {total:.2f}"
      f"\nTOTAL GROWTH IN WEALTH Rs. {balance-total:.2f}"
      f"\nCUMULATIVE ANNUAL GROWTH RATE OF THE PRINCIPAL AMOUNT IS ={cagr*100:.2f}%"
      )
if balance >= target:
    print("This Plan Achieves Your Target".upper())
else:
    print("This Plan Does not Achieve Your Target".upper())
print("__________________________________________________________")
#Conservative Calculation
print("__________________________________________________________")
print("***Conservative Calculation***".upper())
print(f"FINAL AMOUNT {con_balance:.2f}"
      f"\nTOTAL AMOUNT INVESTED {total:.2f}"
      f"\nTOTAL GROWTH IN WEALTH Rs. {con_balance-total:.2f}"
      f"\nCUMULATIVE ANNUAL GROWTH RATE OF THE PRINCIPAL AMOUNT IS ={con_cagr*100:.2f}%"
      )
if con_balance >= target:
    print("This Plan Achieves Your Target.".upper())
else:
    print("This Plan Does not Achieve Your Target.".upper())
print("__________________________________________________________")

