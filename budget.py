#!/usr/bin/python3

######## BRACKETS ########
# bottom,top,percentage
caliBrackets = [ # single
    [0,10099,.01],
    [10100,23942,.02],
    [23943,37788,.04],
    [37789,52495,.06],
    [52496,66295,.08],
    [66296,338639,.093],
    [338640,406364,.103],
    [406365,677275,.113],
    [677276,1000000000,.123],
]
#idahoBrackets = [ # single
#    [0,1540,.0112],
#    [1541,3080,.0312],
#    [3081,4621,.0362],
#    [4622,6161,.0462],
#    [6162,7702,.0562],
#    [7703,11553,.0662],
#    [11554,1000000000,.0692]
#]
fedBrackets = [ # single
    [0,10275,.1],
    [10276,41775,.12],
    [41776,89075,.22],
    [89076,170050,.24],
    [170051,215950,.32],
    [215951,539900,.35],
    [359901,1000000000,.37]
]
spacer = "="*79

######### FUNCTIONS #########
def main(): 
    Budget(ProvideSalary())

def LineItem(item,value,length=60):
    spacer = "-"*(length-len(item))
    return f"{item} {spacer} {value}"

def CalculateTaxes(income,brackets): # FY2022
    taxes = 0
    for b in brackets:
        bottom = b[0]
        top = b[1]
        amount = b[2]
        if income > top:
            taxes += (top - bottom) * amount
        else:
            taxes += (income - bottom) * amount
            break
    return round(taxes,2)

def Budget(grossIncome):
    #idahoTaxes = CalculateTaxes(grossIncome,idahoBrackets)
    caliTaxes = CalculateTaxes(grossIncome,caliBrackets)
    fedTaxes = CalculateTaxes(grossIncome,fedBrackets)
    netIncome = grossIncome-caliTaxes-fedTaxes
    print(
        "\n"+spacer,
        "\nTAX EST.",
        LineItem("\nGross Income:","$"+str(grossIncome)),
        LineItem("\nCalifornia Taxes:","[$"+str(caliTaxes)+"]"),
        LineItem("\nFederal Taxes:","[$"+str(fedTaxes)+"]"),
        LineItem("\nNet Income:","$"+str(netIncome)),
        "\n"+spacer
    )

def ProvideSalary():
    salary = input("How much do you make annually?:\t").split('.')[0] # do not take cents
    filteredSalary = "".join([char for char in salary if char in "0123456789"]) # ignore non-numeric chars
    return int(filteredSalary)
    
# EXECUTE SCRIPT
main()
