'''def sum():
    # this is the first comment
    x,y,z="orange","banana","cherry"
    a=b=c="orange"
    print("hi",a,b,c,x,y,z)
    print(a)
    print(b)
    print(c)
    print(x)
    print(y)
    print(z)
sum()
a=2
b=2.8
print(type(b))
x="dfghjjiuuuuuyg"
print(len(x))
d=input(" please enter youer name")
print("hello",d)
x=input(" please enter the first num")
y=input(" please enter second num")
sum=int(x)+int(y)
print(sum)
name="Betelihem"
age=23
txt="my name is {:s} and I am {:d} years old" 
print(txt.format(name,age))'''
#second lab
'''x="abebe"
print(x[0])
print(x[-1])
print(x[::-1])
y="hello, world"
print(y.split(' , '))'''
'''k=2
h=3.55
print(bin(k))
print(int(h))
num=int(input("enter natural number"))
if(num % 2==0):
    print ("the entered num is even")
else:
    print ("the entered num is odd")
z=int(input("enter a number "))
if(z<=100):
    if(z%3==0):
        print("hello")
    elif(z%5==0):
        print("world")
    else:
        print("the number is not divisible by 5 or 3")
else:
    print("you intered invalid number")
for n in range (100):
    if(n%3==0):
        print("hello")
    elif(n%5==0):
        print("world")
    else:
        print("the number is not divisible by 5 or 3")
x=int(input("enter any number"))
match x: 
    case 2:
        print("two")
    case 4:
        print("four")'''
#3rd day lab
def sum(a,b):
    return a+b
print(sum(2,3))
g=[1,2,3,4]
g.append(50)
del g[0]
print(g)
x=[1,2,3,4,5]
y= x.copy()
y=list(x)
z=[5,]
print(type(z))
a,b,*c=x
print(a)
print(b)
print(c)
stud_info={
"name":["abebe","almaz","bekele"],
"age":['18','16','20'],
"CGPA":['3.2','3.5','2.8']
}
print(stud_info)
set1={"a","s"}
print(type(set1))
def my_sum(*args):
    for i in args:
        print (i)
my_sum(2,3,4,5)