hours = 37
rate = 30
annual = (hours * rate * 4) * 12
pay = hours * rate * 4
vat = annual - (annual * 20 / 100)
print("Monthly Wage: ", pay)
print("Annual wage before vat: ", annual)
print("Annual Wage after vat:  ", vat)