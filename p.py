import random
svar = "j"
while svar == "j":
    tärning1 = random.randrange(6) + 1
    tärning2 = random.randrange(6) + 1
    
    print(tärning1)
    print(tärning2)
    
    
    if tärning1==tärning2:
        print ("vinst 5kr")
    elif tärning1 + 1 == tärning2:
        print ("stege vinst")
    elif tärning1 - 1 == tärning2:
        print ("stege vinst 3")
    elif tärning1 + 5 ==tärning2:
        print ("vinst sexa 3kr")
        
        
    else:
        print ("förlust")
    print("vill du spela j/n: j")
    svar = input("vill du spela j/n: j")

