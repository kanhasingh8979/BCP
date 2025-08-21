'''7. Read three angles of triangles and determine their types(Right triangle, Obtuse 
triangle, Acute triangle). '''
a=int(input("Enter first angle: "))
b=int(input("Enter second angle: "))
c=int(input("Enter third angle: "))
if (a + b + c) == 180:
    print("valid")
    if(a==90 or b==90 or c==90):
        print("right angle triangle")
    elif(a<90 and b<90 and c<90):
        print("acute angle triangle")
    elif(a>90 or b>90 or c>90):
        print("obtuse angle triangle")
else:
    print("invalid tranlge")