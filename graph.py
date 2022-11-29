# One Stop Insurance Company Graph
# Author: Laura Fry     Date: Nov 28, 2022

# Imports
import matplotlib.pyplot as plt
import FormatValues as FV

# User Inputs
claimsJan = float(input("Enter the number of claims for January: "))
claimsFeb = float(input("Enter the number of claims for February: "))
claimsMar = float(input("Enter the number of claims for March: "))
claimsApr = float(input("Enter the number of claims for April: "))
claimsMay = float(input("Enter the number of claims for May: "))
claimsJun = float(input("Enter the number of claims for June: "))
claimsJul = float(input("Enter the number of claims for July: "))
claimsAug = float(input("Enter the number of claims for August: "))
claimsSep = float(input("Enter the number of claims for September: "))
claimsOct = float(input("Enter the number of claims for October: "))
claimsNov = float(input("Enter the number of claims for November: "))
claimsDec = float(input("Enter the number of claims for December: "))

totalsList = [claimsJan, claimsFeb, claimsMar, claimsApr, claimsMay, claimsJun, claimsJul, claimsAug, claimsSep,
        claimsOct, claimsNov, claimsDec]

monthsList = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

plt.bar(monthsList, totalsList)

plt.xlabel('Month')
plt.ylabel('Number of Claims')

plt.title("Total Insurance Claims for the Year")

for x,y in zip(monthsList, totalsList):
        label = "${:,.2f}".format(y)
        plt.annotate(label, (x,y), textcoords="offset points", xytext=(0,10), ha='center', size=6)

plt.show()