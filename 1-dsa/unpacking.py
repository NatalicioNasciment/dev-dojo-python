#1. Unpacking a Sequence into Separate Variables
n = (10,12)

n1, n2 = n 
print(n1)
print(n2)

data = [ 'TEST', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data

_, _, _, (y, m, d) = data

print(name, date, price)
print(y)

