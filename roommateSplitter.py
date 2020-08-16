import gspread

from oauth2client.service_account import ServiceAccountCredentials
from venmo_api import Client

class Roommate:
    def __init__(self, name):
        self.name=name
        self.roommates={}
        self.username=""
        self.password=""
    def addRoommate(self, rname, money):
        self.roommates[rname]=money
    def addVenmo(self):
        self.username=input("What is "+self.name+"'s Venmo username: ")
        self.password=input("What is "+self.name+"'s Venmo password: ") #use stdiomask to hide the text with asterisks
    def receiptPrint(self):
        total=0
        for key in self.roommates.keys():
            key_value=self.roommates.get(key)
            value=float(key_value.split("$")[1])
            
            
            if "-" in key_value:
                value*=-1
            total+=value
            
            if value>0:
                print_value=str(value)
                if print_value.index(".")!=len(print_value)-3: #if we only have one number after the decimal point
                    print_value+="0"
                print("\tExpect to receive $"+print_value+" from",key)
            elif value<0:
                value=abs(value)
                print_value=str(value)
                if print_value.index(".")!=len(print_value)-3: #if we only have one number after the decimal point
                    print_value+="0"
                print("\tPay $"+print_value+" to",key)
            #ignores if value is 0
        total=round(total,2)
        if total<0:
            total=abs(total)
            print_total=str(total)
            if print_total.index(".")!=len(print_total)-3: #if we only have one number after the decimal point
                print_total+="0"
            print("In total, expect to pay $"+print_total)
        elif total>0:
            print_total=str(total)
            if print_total.index(".")!=len(print_total)-3: #if we only have one number after the decimal point
                print_total+="0"
            print("In total, expect to be receive $"+print_total)
        else:
            print("In total, you lose and pay no money!")
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)

client = gspread.authorize(creds)

main_sheet = client.open("Roommates Splitter")

#Get final costs data
receipt_sheet=main_sheet.worksheet("Final Costs")  

sheet = receipt_sheet.get_all_values()
row = sheet.pop(0)

while row.count("Final Calculations")==0:
    row=sheet.pop(0)

house=[]
row=sheet.pop(0)[2:]
for person in row:
    rmate=Roommate(person)
    house.append(rmate)


while len(sheet)>0:
    row=sheet.pop(0)[1:] #ignore the first cell
    name=row[0]
    money=row[1:]
    for index in range(len(money)): #the index to access money aligns with the index of the person in the house list
        amount=money[index]
        house[index].addRoommate(name, amount)

    
for person in house:
    print("\n"+person.name+"'s Venmo To-do list:")
    person.receiptPrint()



    