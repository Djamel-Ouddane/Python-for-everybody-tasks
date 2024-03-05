hours = input("Enter Hours:")
h = float(hours)
rate = input("Enter base rate:")
r = float(rate)
high_rate = 1.5
hr = float(high_rate)
if h >40:
    j=(r*1.5)*(h-40)+(40*r)
if h<=40:
    j=h*r
total = float(j)
print(total)
