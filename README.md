# Compound Growth Simulator

A command-line tool that projects how an investment grows over time based on an
expected return, regular yearly contributions, and inflation.

## The Problem It Solves

Any investor planning for the future faces a simple but hard-to-eyeball question:
"If I start with this much, add a fixed amount every year, and earn roughly this
return, what will I actually have in N years — and what is it really worth once
inflation is accounted for?" This tool answers that question. It projects the
balance year by year, adjusts for inflation to show real purchasing power, and
reports the final amount and growth rate — turning a one-off spreadsheet
calculation into a repeatable program.

## Features

- Year-by-year projection of the investment balance
- Inflation-adjusted ("real") value shown for each year
- Compares investment growth under an optimistic vs a conservative growth rate
- Checks whether the plan reaches a user-defined target amount
- Reports the cumulative annual growth rate (CAGR) of the principal for both scenarios

## Limitations
- It only calculates CAGR on "Principal Amount" entered
- Data types must be correct

## How to Run It

This is a Python script, run from the terminal:

```
python "Compound Growth Simulator.py"
```
The program then asks you to enter: principal amount, expected inflation %,
optimistic growth rate %, conservative growth rate %, annual contribution,
number of years, and your target amount.

## Example Run

```
Welcome Dear!

CUMULATIVE ANNUAL GROWTH RATE CALCULATOR
By Muhammad Naseer
--------------------

Please insert the principal amount (Rs.) = 1000000
Please insert the expected inflation value % = 12
Please insert the expected (optimistic) growth rate % = 14
Please enter your a conservative growth rate % = 11
Please insert the annual contribution (Rs.) = 120000
Please insert the number of years for investment = 15
What is your target to achieve? Enter Amount Rs. = 5000000
---Year 1---
Your Balance for the year is Rs. 1260000.00.
Your Balance for the Year based on Conservative Growth rate is Rs. 1230000.00.
Your Real Growth is Rs. 1125000.00.
Your Real Growth based on conservative growth rate is Rs. 1098214.29.
---Year 2---
Your Balance for the year is Rs. 1556400.00.
Your Balance for the Year based on Conservative Growth rate is Rs. 1485300.00.
Your Real Growth is Rs. 1240752.55.
Your Real Growth based on conservative growth rate is Rs. 1184072.07.
---Year 3---
Your Balance for the year is Rs. 1894296.00.
Your Balance for the Year based on Conservative Growth rate is Rs. 1768683.00.
Your Real Growth is Rs. 1348322.48.
Your Real Growth based on conservative growth rate is Rs. 1258913.62.
---Year 4---
Your Balance for the year is Rs. 2279497.44.
Your Balance for the Year based on Conservative Growth rate is Rs. 2083238.13.
Your principal amount is doubled.
Your principal amount is also doubled based on conservative growth rate.
Your Real Growth is Rs. 1448661.83.
Your Real Growth based on conservative growth rate is Rs. 1323935.49.
---Year 5---
Your Balance for the year is Rs. 2718627.08.
Your Balance for the Year based on Conservative Growth rate is Rs. 2432394.32.
Your principal amount is doubled.
Your principal amount is also doubled based on conservative growth rate.
Your Real Growth is Rs. 1542622.02.
Your Real Growth based on conservative growth rate is Rs. 1380205.86.
---Year 6---
Your Balance for the year is Rs. 3219234.87.
Your Balance for the Year based on Conservative Growth rate is Rs. 2819957.70.
Your principal amount is doubled.
Your principal amount is also doubled based on conservative growth rate.
Your Real Growth is Rs. 1630964.57.
Your Real Growth based on conservative growth rate is Rs. 1428678.33.
---Year 7---
Your Balance for the year is Rs. 3789927.76.
Your Balance for the Year based on Conservative Growth rate is Rs. 3250153.05.
Your principal amount is doubled.
Your principal amount is also doubled based on conservative growth rate.
Your Real Growth is Rs. 1714370.85.
Your Real Growth based on conservative growth rate is Rs. 1470204.18.
---Year 8---
Your Balance for the year is Rs. 4440517.64.
Your Balance for the Year based on Conservative Growth rate is Rs. 3727669.88.
Your principal amount is doubled.
Your principal amount is also doubled based on conservative growth rate.
Your Real Growth is Rs. 1793450.60.
Your Real Growth based on conservative growth rate is Rs. 1505543.34.
---Year 9---
Your Balance for the year is Rs. 5182190.11.
Your Balance for the Year based on Conservative Growth rate is Rs. 4257713.57.
Your principal amount is doubled.
Your principal amount is also doubled based on conservative growth rate.
Your Real Growth is Rs. 1868749.71.
Your Real Growth based on conservative growth rate is Rs. 1535374.20.
---Year 10---
Your Balance for the year is Rs. 6027696.73.
Your Balance for the Year based on Conservative Growth rate is Rs. 4846062.06.
Your principal amount is doubled.
Your principal amount is also doubled based on conservative growth rate.
Your Real Growth is Rs. 1940757.02.
Your Real Growth based on conservative growth rate is Rs. 1560302.29.
---Year 11---
Your Balance for the year is Rs. 6991574.27.
Your Balance for the Year based on Conservative Growth rate is Rs. 5499128.89.
Your principal amount is doubled.
Your principal amount is also doubled based on conservative growth rate.
Your Real Growth is Rs. 2009910.53.
Your Real Growth based on conservative growth rate is Rs. 1580868.15.
---Year 12---
Your Balance for the year is Rs. 8090394.67.
Your Balance for the Year based on Conservative Growth rate is Rs. 6224033.07.
Your principal amount is doubled.
Your principal amount is also doubled based on conservative growth rate.
Your Real Growth is Rs. 2076602.80.
Your Real Growth based on conservative growth rate is Rs. 1597554.27.
---Year 13---
Your Balance for the year is Rs. 9343049.92.
Your Balance for the Year based on Conservative Growth rate is Rs. 7028676.70.
Your principal amount is doubled.
Your principal amount is also doubled based on conservative growth rate.
Your Real Growth is Rs. 2141185.90.
Your Real Growth based on conservative growth rate is Rs. 1610791.29.
---Year 14---
Your Balance for the year is Rs. 10771076.91.
Your Balance for the Year based on Conservative Growth rate is Rs. 7921831.14.
Your principal amount is doubled.
Your principal amount is also doubled based on conservative growth rate.
Your Real Growth is Rs. 2203975.74.
Your Real Growth based on conservative growth rate is Rs. 1620963.60.
---Year 15---
Your Balance for the year is Rs. 12399027.67.
Your Balance for the Year based on Conservative Growth rate is Rs. 8913232.57.
Your principal amount is doubled.
Your principal amount is also doubled based on conservative growth rate.
Your Real Growth is Rs. 2265256.00.
Your Real Growth based on conservative growth rate is Rs. 1628414.27.
Your Cumulative Annual Growth Rate of the principal amount (CAGR) is 18.27%.
---SUMMARY---
__________________________________________________________
***OPTIMISTIC CALCULATION***
FINAL AMOUNT 12399027.67
TOTAL AMOUNT INVESTED 2800000.00
TOTAL GROWTH IN WEALTH Rs. 9599027.67
CUMULATIVE ANNUAL GROWTH RATE OF THE PRINCIPAL AMOUNT IS =18.27%
THIS PLAN ACHIEVES YOUR TARGET
__________________________________________________________
__________________________________________________________
***CONSERVATIVE CALCULATION***
FINAL AMOUNT 8913232.57
TOTAL AMOUNT INVESTED 2800000.00
TOTAL GROWTH IN WEALTH Rs. 6113232.57
CUMULATIVE ANNUAL GROWTH RATE OF THE PRINCIPAL AMOUNT IS =15.70%
THIS PLAN ACHIEVES YOUR TARGET.
```
## Author
Muhammad Naseer
