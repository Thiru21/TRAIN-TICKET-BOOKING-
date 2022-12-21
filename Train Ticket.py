from pymongo import MongoClient
import random as ra
client=MongoClient("mongodb://localhost:27017")
db=client["Train_ticket"]
coll=db["booking"]
dum=db["booking"]
print("Ticket Booking")
fs = []
ts = []
jd = []
def Train():
    T = ra.randint(0,24)
    M = ra.randint(0,59)
    FS = str(input("\nArrival:"))
    fs.append(FS)
    TS = str(input("\nDeparture:"))
    ts.append(TS)
    JD = int(input("\nJourney Date:"))
    jd.append(JD)
    dum.insert_one({"Arrival":FS,"Departure":TS,"Journey_Date":JD})
    if JD in range(1, 32):
        print("\nTrain Details")
        if JD <= 15:
            print(FS, "EXP (124566)")
            print("Time:", T,":",M)
            print("Arrival:", FS)
            print("Date:", JD)
        elif JD <= 26:
            print(FS, "EXP (223148)")
            print("Time:", T,":",M)
            print("Arrival:", FS)
            print("Date:", JD)
        elif JD <= 32:
            print(FS, "EXP (356712)")
            print("Time:", T,":",M)
            print("Arrival:", FS, )
            print("Date:", JD)
    else:
        print("\nType vaild Number")
        Train()
Train()
def detail():
    Tic = int(input("\nEnter No.Of Ticket:"))
    Name = []
    Age = []
    Gender = []
    def people():
        for passenger in range(Tic):
            name = str(input("\nName:"))
            Name.append(name)
            age = int(input("\nAge:"))
            Age.append(age)
            gender = str(input("\nGender:"))
            Gender.append(gender)
            dum.insert_one({"Name":name,"Age":age,"gender":gender})
    people()
    def Ticket():
        x = 0
        print("\nTotal Ticket : ", Tic)
        print("\nArrival:", fs[x])
        print("\nDeparture:", ts[x])
        print("\nJourney Date:", jd[x])
        for passenger in range(1,Tic + 1):
            print("\nName:", Name[x])
            print("\nAge:", Age[x])
            print("\nGender:", Gender[x])
            x += 1
    Ticket()
detail()
details=str(input("\nDid you forgot someone? no/yes:"))
if details in ("yes","YES","y","Y"):
    detail()
