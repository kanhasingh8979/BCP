#6. Read three integers and print their maximum. 
a=int(input());
b=int(input());
c=int(input());
if a<b and a<c:
    print("a is minimum");
elif b<c:
    print("b is minimum");
else :
    print("c is minimum");