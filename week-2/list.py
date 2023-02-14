names=["John","Mary","James","Jude","Amy"]
#Accessing items in a list
print (names)
print(names[0])

print(names[-1])
print(names[2])
print(names[0:3])
#create a list of fruits
fruits=["mangoes","oranges","apples","grapes","kiwi","avocadoes","watermelon"]
print(fruits)
print(fruits[3])
print("My favourite fruit is :",fruits[3])
print(fruits[1].upper())
#Adding two lists
vegetables=["kales","spinach","carrot","brocolli","cabbage"]
stationary= ["pens","sharpener","ruler","rubber","highlighter"]
shoppings= (vegetables) + (stationary)
print(shoppings)
print(shoppings[5])
for vegetable in vegetables: 
    print(vegetable)
    for shopping in shoppings:
        print(shopping)
        print("My name is ")+ names[0]("and my favourite fruit is"+fruits[4])