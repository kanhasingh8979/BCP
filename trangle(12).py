'''12. You are given 3 integer angles(in degrees), A, B, and C, of a triangle. You have to tell 
whether the triangle is valid or not. A triangle is valid if the sum of its angles equals 
180. '''
a=int(input("Enter first angle: "));
b=int(input("Enter second angle: "));
c=int(input("Enter third angle: "));
if(a+b+c)==180:
    print("valid");
else:
    print("invalid");