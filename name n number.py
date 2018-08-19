n=input("Enter string")
m=input("Enter mobile number")
a=len(n)
b=len(m)
if((a>=3)==True and n.isalpha()==True and (b==10)==True and m.isalnum()==True ):
    print("valid data")
else:
    print("invalid data")
