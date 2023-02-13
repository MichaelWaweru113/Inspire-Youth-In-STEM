#write a program to get the compound interest
p= input("Enter principle amount :")
r= input("Enter rate :")
n= input("Enter number of years :")
compound_interest= int(p)*((1+ int(r)/100)**int(n))
print(compound_interest)