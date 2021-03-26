from src.ReadCSVFile import *

def loadCustomers():
    customerData = getFileData("customer.csv")
    return customerData

def formatCustomers():
    display = ""
    customerData = loadCustomers()
    for counter in range(1,len(customerData)):
        display += customerData[counter] + "\n"
    return display