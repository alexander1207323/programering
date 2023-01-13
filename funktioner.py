# 1 Kelvin till Celsius


def omvandla_kelvin_till_farenheight(farenheight):
    farenheight= (kelvin -273)*(9.0/5.0) + 32
    return farenheight
k = float(input("ange temperatur i kelvin "))
c = omvandla_kelvin_till_farenheight(k)

print(k, "farenheight")

 

