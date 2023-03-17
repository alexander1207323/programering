svar=input("gissa på tal")
tal = int(svar)
while not tal==42:

    if tal<42:
        
        print("gisning litet")
        svar=input("gissa på tal")
        tal = int(svar)
    elif tal>42:
        print("gisning för stort")
        svar=input("gissa på tal")
        tal = int(svar)
        
    
print("gisning rätt")       
    



