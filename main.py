# ONE STOP INSURANCEE COMPANY
# Author: Laura Fry    Date: Nov 23, 2022

# Imports
import FormatValues as FV
import datetime
import calendar

# Code to add data to the data file.
nextPolicyNum = 1944
basicPremium = 869.00
discountAdditionalCars = .25
costExtraLiability = 130.00
costGlassCoverage = 86.00
costLoanerCar = 58.00
HST_RATE = .15
processingFee = 39.99

f = open("../../Desktop/OSICDef.dat", "w")

f.write("{}\n".format(nextPolicyNum))
f.write("{}\n".format(basicPremium))
f.write("{}\n".format(discountAdditionalCars))
f.write("{}\n".format(costExtraLiability))
f.write("{}\n".format(costGlassCoverage))
f.write("{}\n".format(costLoanerCar))
f.write("{}\n".format(HST_RATE))
f.write("{}\n".format(processingFee))

f.close()

# Start of program to calculate new insurance policy information.
while True:

    # User Inputs
    custFN = input("Enter the customer's first name: ").title()
    custLN = input("Enter the customer's last name: ").title()
    address = input("Enter the customer's address: ")
    city = input("Enter the customer's city: ")
    province = input("Enter the customer's province: (ex: NL) ")
    postalCode = input("Enter the customer's postal code: ")
    phoneNum = input("Enter the customer's phone number: ")
    numCarsInsured = int(input("Enter the number of cars being insured: "))
    extraLiabilityOption = input("Would you like extra liability up to $1,000,000? (Y/N) ").upper()
    glassCoverageOption = input("Would you like glass coverage? (Y/N) ").upper()
    loanerCarOption = input("Would you like a loaner car? (Y/N) ").upper()
    paymentOption = input("Would you like to pay in full or monthly? (F/M) ").upper()

    # Calculations
    if numCarsInsured == 1:
        insurancePremiums = basicPremium
    elif numCarsInsured > 1:
        insurancePremiums = basicPremium + (numCarsInsured - 1) * (basicPremium * (1 - discountAdditionalCars))

    totalExtraCosts = 0
    if extraLiabilityOption == "Y":
        totalExtraCosts += costExtraLiability

    if glassCoverageOption == "Y":
        totalExtraCosts += costGlassCoverage

    if loanerCarOption == "Y":
        totalExtraCosts += costLoanerCar

    totalInsurancePremium = insurancePremiums + totalExtraCosts
    HST = totalInsurancePremium * HST_RATE
    totalCost = totalInsurancePremium + HST

    monthlyPayment = (totalCost + processingFee) / 8

    # BONUS: Monthly Payment Date
    # Policy Date
    policyDate = datetime.datetime.now()
    year = policyDate.year
    month = policyDate.month
    days = calendar.monthrange(year, month)[1]

    # Following Month
    followingMonth = policyDate.month + 1
    if followingMonth == 13:
        followingYear = policyDate.year + 1
        followingMonth = 1
        followingDays = calendar.monthrange(followingYear, followingMonth)[1]
    else:
        followingDays = calendar.monthrange(year, followingMonth)[1]

    # First Payment Date
    if policyDate.day <= 25:
        daysDifference = days - policyDate.day
        firstPaymentDate = policyDate + datetime.timedelta(days=daysDifference + 1)
    else:
        daysDifference = days - policyDate.day
        firstPaymentDate = policyDate + datetime.timedelta(days=daysDifference + 1 + followingDays)

    # Receipt
    print()
    print("       One Stop Insurance Company       ")
    print()
    print("****************************************")
    print("Customer Name: " + custFN, custLN)
    print("Customer Phone Number: " + phoneNum)
    print("Customer Address:", address)
    print("                 ", city + ",", province)
    print("                 ", postalCode)
    print("****************************************")
    print("Number of Cars Insured:", numCarsInsured)
    print("Extra Liability:", extraLiabilityOption)
    print("Glass Coverage:", glassCoverageOption)
    print("Loaner Car:", loanerCarOption)
    print("Payment Option:", paymentOption)
    print("****************************************")
    print(f"Insurance Premiums:           {FV.FDollar2(insurancePremiums):>10s}")
    print(f"Total Extra Costs:            {FV.FDollar2(totalExtraCosts):>10s}")
    print(f"Total Insurance Premium:      {FV.FDollar2(totalInsurancePremium):>10s}")
    print(f"HST:                          {FV.FDollar2(HST):>10s}")
    print(f"Total Cost:                   {FV.FDollar2(totalCost):>10s}")
    print("****************************************")
    if paymentOption == "M":
        print(f"Monthly Payments:             {FV.FDollar2(monthlyPayment):>10s}")
        firstPaymentDateStr = firstPaymentDate.strftime("%Y-%m-%d")
        print(f"First Payment Date:           {firstPaymentDateStr:>10s}")
        print("****************************************")
    policyNumStr = str(nextPolicyNum)
    print("Policy Number:", policyNumStr + "-" + custFN[0] + custLN[0])

    # Code to save the policy information.
    f = open("Policies.dat", "a")

    f.write("{}, ".format(nextPolicyNum))
    policyDateStr = policyDate.strftime("%Y-%m-%d")
    f.write("{}, ".format(policyDateStr))
    f.write("{}, ".format(custFN, custLN))
    f.write("{}, ".format(address))
    f.write("{}, ".format(city))
    f.write("{}, ".format(province))
    f.write("{}, ".format(postalCode))
    f.write("{}, ".format(phoneNum))
    f.write("{}, ".format(numCarsInsured))
    f.write("{}, ".format(extraLiabilityOption))
    f.write("{}, ".format(glassCoverageOption))
    f.write("{}, ".format(loanerCarOption))
    f.write("{}, ".format(paymentOption))
    f.write("{}\n".format(totalInsurancePremium))

    print()
    print("Policy information processed and saved.")
    print()
    nextPolicyNum += 1

    choice = input("Would you like to process another customer? (Y/N) ").upper()
    print()
    if choice == "N":
        break

    f.close()

    # Code to write current values back to the defaults file.
    f = open("../../Desktop/OSICDef.dat", "w")

    f.write("{}\n".format(nextPolicyNum))
    f.write("{}\n".format(basicPremium))
    f.write("{}\n".format(discountAdditionalCars))
    f.write("{}\n".format(costExtraLiability))
    f.write("{}\n".format(costGlassCoverage))
    f.write("{}\n".format(costLoanerCar))
    f.write("{}\n".format(HST_RATE))
    f.write("{}\n".format(processingFee))

    f.close()

