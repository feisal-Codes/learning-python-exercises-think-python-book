inventory={}
prices={'milk':50,'soda':30,'water500ml':25}

def userInput():
    while True:
     global inventory
     item=input("Please Enter item's Name:or Q to Quit " )
     if item.upper()=="Q":
           break
     try:
      itemNumber=int(input("Please Enter item's Quantity "))
     except ValueError:
        print("Enter A Number")
     return(item,itemNumber)
def StockIn():
    item,itemNumber=userInput()
    inventory[item]=itemNumber
def getStock():
    return inventory
def StockOut():
    global prices 
    global inventory
    item,itemNumber=userInput()
    inventory[item]-= itemNumber
    if item in prices:
        value=prices[item]
        print(itemNumber*value)
        


def main():
    StockIn()
    print(getStock())
    print('****************')
    StockOut()
    print(getStock())
    print('****************')
    print('****************')


    
main()