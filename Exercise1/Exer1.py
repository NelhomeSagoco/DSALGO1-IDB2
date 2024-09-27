'''
x=1 #integer
y=2.0 #real number
z=x*y #multiplication operation and the result is a real number
print("1 x 2.0",z,"\n This is a test for my python program") #print statement

This is a multi line comment

userInput = input("How old Are You?") #Accepting an input with a prompt message
print(userInput,"years old!") #prints out the userinput

userInput = int(input ("Enter a Number: "))
userInput2 = int(input ("Enter a Number Again: "))
sum = userInput + userInput2
print("The sum is: " , sum)

'''

'''
NintendoWiisprice = 100
print("Welcome to Nintendo Wiis")
userMoney = int(input ("Enter the amount of Money You Have: "))
totalBuy = int(userMoney / NintendoWiisprice)
print("You Can Buy",totalBuy,"pieces of Nintendo Wiis")
change = userMoney - (NintendoWiisprice * totalBuy)
print("You Have a Balance of",change)
afford = NintendoWiisprice-(userMoney % NintendoWiisprice)
print("You are lacking", afford, "to get another Nintendo Wiis")
'''

'''
factorial=1
x = int(input("Enter a number: "))
for x in range(1, x+1):
    factorial = factorial*x
print("The factorial of", x,"is",factorial)'''

'''  
x = int(input("Enter a Number: "))
for a in range (1, x+1):
    if x%a ==0:
        print(a, "is a factor of ",x,".")
'''

factorlist =[]
x= int(input("Enter A number: "))
for a in range  (1, x+1):
    if x%a ==0:
        factorlist.append(a)
print("The factors of ",x, "are: ", factorlist)

