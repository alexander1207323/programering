svar=input("gissa på tal")
tal = int(svar)
while not tal==42:

    if tal<42:
        
        print("gisning litet")
        svar=input("gissa på tal")
        tal = int(svar)
    elif tal>42:
        print("gisning stort")
        svar=input("gissa på tal")
        
    
print("gisning rätt")       
    



