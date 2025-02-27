# length=float(input("enter the number :"))
# if length<0:
#     print("invalid entry")
# else:
#     inch=length/2.54
#     print(inch,"inch")
# t=int(input("enter the time"))
# t1=int(input ("enter the ahead time :"))
# if t+t1<=12:
#     print(t+t1)
# else:
#     print(12-(t+t1)-12)
# a=int(input("enter the number "))
# b=int(input("enter the number"))
# if a-b==0.001:
#     print("close")
y=int(input("enter the number" :))
if (y%100!=0 and y%4==0) or y%400==0:
    print("leap year")
else:
    print("not a leap year")