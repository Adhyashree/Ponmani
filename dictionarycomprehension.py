def discount(k,v):
    if(k=='bag'or k=='pen'):
        v=round(v*.95)
    return v
cart={'table':23000.10,'bag':650.00,'pen':30.56,'chair':5500.235}
print(cart)
cart1={k:round(v)  for (k,v) in cart.items()}
print(cart1)
cart2={k:round(v*.9)  for (k,v) in cart.items() if v>10000}
print(cart2)
cart3={k:round(v*.9) if v>5000 else round(v)  for (k,v) in cart.items()}
print(cart3)
cart4={k:discount(k,v)  for (k,v) in cart.items()}
print(cart4)
items=["table",'pen',"lamp"]
cost=[1200,560,2350]
stock=[10,5,6]
zipped={k:v for(k,v) in zip(items,cost)}
print(zipped)
zipped1=list(zip(items,cost,stock))
print(zipped1)