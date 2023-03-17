from random import randint

raknare = 0

n = int(input("Ange antalet kast: "))

#Kör loopen från 0 till n - 1, dvs n gånger
for i in range(n):
    #randint(a, b) slumpar fram ett heltal x, a <= x <= b
    tarning1 = randint(1, 6)
    tarning2 = randint(1, 6)
    #Om tärningarna visar lika
    if(tarning1 == tarning2):
        #Räkna antalet gynnsamma utfall
        raknare = raknare + 1