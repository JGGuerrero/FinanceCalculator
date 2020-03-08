import math


presentValue = input("What is PV?")
futureValue = input("What is FV?")
rate = input("What is the Rate?")
pmt = 0
nper = input("What is the amount of Periods?")
m = input("How many times in a period is it compounded?")

# RATE FORMULA============================================================================================================================

if (rate.isalpha()):
    rate = ((int(futureValue)/int(presentValue))**(1/int(nper))-1)*100
    print("Rate is: ", round(rate, 2))

# ===========================================================================================================================================

# FUTURE VALUE FORMULAS========================================================================================================================

elif (((futureValue.isalpha()) & (int(m)>1))):
    futureValue = int(presentValue)* ((1 + (float(rate) / int(m)))**(int(m)*int(nper)))
    print("Compounded Future Value is: ", round(futureValue, 2))

elif (futureValue.isalpha()):
    futureValue = int(presentValue)*math.exp(float(rate)*int(nper))
    print("Future Value is: ", round(futureValue, 2))

# ========================================================================================================================================

# PERIOD FORMULA==========================================================================================================================

elif (nper.isalpha()):
    nper = (math.log(int(futureValue)/int(presentValue)))/(math.log(1+float(rate)))
    print("The amount of periods is: ", round(nper, 6))

# ======================================================================================================================================

# PRESENT VALUE FORMULA ================================================================================================================

elif ((presentValue.isalpha()) & (int(m) > 1)):
    presentValue = int(futureValue) / ((1 + round(float(rate)/int(m), 6)))**(int(nper)*int(m))
    print("Present Value is: ", round(presentValue, 4))

elif (presentValue.isalpha()):
    presentValue = int(futureValue) / ((1 + float(rate)))**int(nper)
    print("Present Value is: ", round(presentValue, 4))

# ======================================================================================================================================
else:
    print("ERROR - CHECK IF FUTURE VALUE IS CONT OR COMPOUNDED")