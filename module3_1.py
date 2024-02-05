def get_total():
    total = float(input("What is the total: "))
    return total

def calc_tip(preTaxTotal):
    tip = float(preTaxTotal) * 0.18
    return tip

def calc_sales_tax(preTaxTotal):
    salesTax = float(preTaxTotal) * 0.07
    return salesTax

def put_total():
    preTaxTotal = "{:.2f}".format(get_total())
    tip = "{:.2f}".format(calc_tip(preTaxTotal))
    salesTax = "{:.2f}".format(calc_sales_tax(float(preTaxTotal)))
    total = float(preTaxTotal) + float(tip) + float(salesTax)
    print(f"The total before tax and tip is ${preTaxTotal}.\nThe sales tax is ${salesTax}.\nThe tip is ${tip}.\nThe total with the tip and sales tax is ${total}.")

put_total()