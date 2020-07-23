print("Hello! This is Sreeja's Flight Booking Service!")
n=input("Enter your first and last name:")
print("Available flights:")
print("1. CMH to JFK")
print("2. DFW to LAX")
print("3. ORD to ATL")
print("4. BOS to FLL")
print("5. LGA to LAS")
print("6. JFK to HND")
print("7. ORD to SIN")
print("8. ORD to DXB")
print("9. LAX to LHR")
print("10. MSY to MCO")
flight=int(input("Choose a flight #:"))
if(flight==1):
    distance=566.3
    time="1 hour 57 minutes"
    cost=92
elif(flight==2):
    distance=1446.1
    time="3 hours 8 minutes"
    cost=51
elif(flight==3):
    distance=744.5
    time="2 hours 13 minutes"
    cost=41
elif(flight==4):
    distance=1478.1
    time="3 hours 7 minutes"
    cost=37
elif(flight==5):
    distance=2539.5
    time="7 hours 30 minutes"
    cost=129
elif(flight==6):
    distance=3440
    time="14 hours 10 minutes"
    cost=1032
elif(flight==7):
    distance=9346
    time="20 hours 15 minutes"
    cost=479
elif(flight==8):
    distance=7229
    time="15 hours 0 minutes"
    cost=775
elif(flight==9):
    distance=5456
    time="11 hour 25 minutes"
    cost=992
else:
    distance=657.8
    time="1 hour 49 minutes"
    cost=37
print("In-flight services (reply with yes or no):")
k=int(input("If you would like In-Flight WiFi for $30, enter 1, if not, enter 0:"))
if(k==1):
    cost=cost+30
else:
    cost=cost+0
    
j=int(input("If you would like In-Flight food services for $15?, enter 2, if not, enter 0:"))
if(j==2):
    cost=cost+15
else:
    cost=cost+0
def frequentflyermiles(cost):
    o=int(input("enter how many frequent flyer miles you have at the moment:"))
    ffm=o+(cost//100)
    if (ffm>8):
        print("congrats! you have enough frequent flyer miles to get a $100 discount")
        t=input("apply discount (reply with 1 if yes, 0 if no)?:")
        if(t==1):
            cost=cost-100
        else:
            ("sorry, you don't have enough frequent flyer miles to get a discount")
            cost=cost-0
    return cost
frequentflyermiles(cost)
print("Flight information: ""Passenger Name:",n,", ""Flight Distance:",distance,"miles , ""Time in Flight:",time,", ""Cost: $",cost)
    
