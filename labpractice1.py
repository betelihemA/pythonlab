###Haymanot 
###Day1
###this is comment section

### x,y,z="Orange","Banana","Cherry"
### print(x)
### print(y)
### print(z)
### x=y=z="Orange"
### print(x)
### print(y)
### print(z)
### a=2
###b=2.1
###print(type(a))
###print(type(b))
###c="haymanot"
###print(lengit pull(c))
###d=input("Enter your name: ")
###print(d)
###print(type(d))
###e=input("Enter first number: ")
###f=input("Enter second number: ")
###g=int(e)+int(f)
###print(g)
###print(ord('g'))
name="someone"
age=23
txt="My name is {:s} and I am {:d} years old"
print(txt.format(name,age))
def sum():
    print("Hello")
sum()
###Day 2
x="abebe"
print(x[0])
print(x[0:2])
print(x[-4:])

print(hex(60))
print(int(4.022221))
num=int(input("Enter a number: "))
if(num%2==0):
    print("Even")
else:
    print("Odd")
for num1 in range(100):
###num1=int(input("Enter a number: "))

   if(num1<100):
     if(num1%3==0 and num1%5==0):
        print("Hello World")
     elif(num1%3==0):
        print("Hello")
     elif(num1%5==0):
        print("World")
x=int(input("Please Enter any Number:"))
match x:
   case 2:
      print("Two")
   case 4:
      print("Four")
