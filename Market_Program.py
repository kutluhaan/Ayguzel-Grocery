# ACCOUNTING PROGRAM

import smtplib

file = open("price_list.txt", "r", encoding="utf-8")

file2 = file.readlines()

for i in range(len(file2)):
    a = file2[i].replace(" sale price", "").replace("TL", "$").split(": ")
    file2.append(a)

file2.reverse()
b = len(file2)
c = b/2
c = int(c)

for i in range(c):
    file2.pop()

stock = {}
for i in range(c):
    stock[file2[i][0]] = file2[i][1]

product = list(stock.keys())
prices = list(stock.values())
print(prices)
for i in range(len(product)):
    print(product[i]+":", prices[i])

buy = str(input("\n" + "Please copy and paste the name(s) of the product you want to buy from the list above: " + "\n"))

basket = []
while True:
    basket.append(buy)
    buy = str(input("\n" + "Is there any thing you want to add your basket?" + "\n"))
    if buy == "no":
        break

mylist = []

for i in range(len(basket)):
    mylist.append(basket[i])
    mylist.append(stock[basket[i]])
    print("\n" + basket[i] + ": " + stock[basket[i]] + "\n")

acknowledge = input("Do you acknowledge the basket? " )

length = len(mylist)
length = length/2
length = int(length)
for i in range(length+1):
    mylist[i] = mylist[i].replace(" $\n", "")

mylist[-1] = mylist[-1].replace(" $\n","")

bill = open("bill.txt", "w")
info = "AYGUZEL GROCERY" + "\n" + "\n"
bill.write(info)

for i in range(length):
    content = basket[i] + ": "
    bill.write(content)
    x = stock[basket[i]]
    x = str(x)
    content2 = x + "\n"
    bill.write(content2)
bill = open("bill.txt", "r")
fileassigned = bill.read()

for i in range(len(prices)):
    prices2 = prices[i].replace(" $","")
    if acknowledge == "yes":
        prices.append(prices2)

prices.reverse()

d = len(prices)
e = d/2
e = int(e)

for i in range(e):
    prices.pop()

for i in range(len(prices)):
    prices[i] = prices[i].replace("\n", "")
    prices[i] = float(prices[i])


for i in range(len(prices)):
    stock[file2[i][0]] = prices[i]

cost = []
for i in range(len(basket)):
    g = stock[basket[i]]
    cost.append(g)

charge = sum(cost)
charge = str(charge)
print("\n" + "Your bill:")


for i in range(len(basket)):
    print("\n" + basket[i] +":", stock[basket[i]], "\n")
print("-------------------------------------")
print("Total:      ", charge)
lastinfo = "-------------------------------------" + "\n" + "Total:      " + charge + "\n" + "Thank you!" + "\n"
bill = open("bill.txt", "a")
bill.write(lastinfo)
bill = open("bill.txt", "r")
fileassigned = bill.read()

approval = str(input("\n" + "Do you approve the bill?" + "\n"))

if approval == "yes":
    sender_email = str(input("Please enter your e-mail: "))
    rec_email = str(input("Please enter the receiver e-mail: "))
    password = str(input("Please enter your password: "))
    message = fileassigned

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    print("Login succesful.")
    server.sendmail(sender_email, rec_email, message)
    print("E mail has been sent to" ,rec_email, "." + "\n" + "Thank you for using Aygüzel Shop")
else:
    print("Basket canceled.")