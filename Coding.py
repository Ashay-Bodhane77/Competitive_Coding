# # #python is dynamically typed language
# # math=40
# # pi=3.14
# # name='Ashay'
# # print(type(math))
# # print(type(pi))
# # print(type(name))    cl

# #typecasting
# print(2+2)
# print("2"+"2")
# print(int("2")+int("2"))
# print(str(2)+str(2))
# val1=input("Enter first number:")#by default input is string
# val2=input("Enter second number:")      
# print(val1+val2) #concatenation
# print(int(val1)+int(val2)) #addition

# # #type conversion
# print(int(3.14)) #float to int
# print(int(True))
# print(int(False))
# print(int(4))
# # print(int("3.14")) #error
# print(int("3")) #string to int
# print(int("swap")) #string to int ValueError: invalid literal for int() with base 10: 'swap'




#float
# print(float(3)) #int to float
# print(float(True))      
# print(float(False))
# print(float(3.14))      
# print(float("3.14")) #string to float
# print(float("swap")) #string to float ValueError: could not convert string to float: 'swap'
# print(float(50+2j)) #complex    to float error: can't convert complex to float  




# #Complex
# print(complex(3)) #int to complex
# print(complex(3.14)) #float to complex      
# print(complex(True))
# print(complex(False))
# print(complex("3.14")) #string to complex
# # print(complex("swap")) #string to complex ValueError: complex() arg is a malformed
# print(complex(50+2j)) #complex to complex
# print(complex("6"))
# print(complex(5,-3)) #real,imaginary    



# #Boolean if we want to convert any value to boolean then we can use bool() function but if we pass 0 in flot ,imaginary,boolean
#  then it will return False otherwise it will return True if we pass zero ,empty string and false value then it will return False otherwise it will return True

#WAP for simple interest
# p=int(input("Enter principal amount:"))
# r=float(input("Enter rate of interest:"))
# t=int(input("Enter time in years:"))    
# si=(p*r*t)/100
# print("Simple Interest is:",si)
# #wap to centigrade to fahrenheit
# c=float(input("Enter temperature in centigrade:"))  
# f=(c*9/5)+32
# print("Temperature in fahrenheit is:",f)

#val1=4
# val2=5
# # temp=val1
# # val1=val2
# # val2=temp
# # print("which was 4 now ",val1)
# # print("which was 5 now ",val2)

# val1=val1+val2
# val2=val1-val2  
# val1=val1-val2
# print("which was 4 now ",val1)
# print("which was 5 now ",val2)

# #reverse A seven digit number

# num=1234567
# rev=0   
# while num>0:
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10 
# print("rev ",rev)


#mylist = ["Ashay", "YASH" ,54 , "Vedant", "Satyarth", 77 ,  "Shivam", "Raghav", "Satyarth",60.50 , "Shivam", "Raghav"]

# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:10:2])
# print(mylist[1:8:3])
# print(mylist[:])
# print(mylist[::-1])
#------------------------------------------------------------------------------------------
# mylist.append("Jai")
# mylist.append("Shree")
# print(mylist)
#------------------------------------------------------------------------------------------
# mylist.insert(1,"Ram")
# print(mylist)
#------------------------------------------------------------------------------------------
# mylist.remove("Satyarth")
# print(mylist)
#------------------------------------------------------------------------------------------
# newlist = mylist.copy()
# print(mylist)
# print(newlist)

#------------------------------------------------------------------------------------------
# mylist = [['prashant', 'jha'], ['89.6'], [440015 , "yyy"]]
# print("Example of multidimensional list")
# print(mylist)
# #print(mylist[row][column])
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])
#--------------------------
# [        0         1
# 0   ['prashant', 'jha'], 
# 1   ['89.6'], 
# 2   [440015 , "yyy"]]
#------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
# list1 = ["prashant", "jha"]
# print (list1*2)

#------------------------------------------------------------------------------------------
# list2 = [50, 22.50]
# print(list1 + list2)

#------------------------------------------------------------------------------------------
# list2 = [50, 22.50 , 'Prashant']
# del list2[0]
# print(list2)

#------------------------------------------------------------------------------------------
# list2 = [50, 22.50 , 'Prashant']
# list2.clear()
# print(list2)

#------------------------------------------------------------------------------------------
# name = "Prashant"
# print(name)
# myname = list(name)
# print(myname)

#------------------------------------------------------------------------------------------
# Sorting example
# mylist = [50, 22 , 11, 60, 3 , 89, 77]
# #mylist.sort()
# mylist.sort(reverse=True)
# print(mylist)

# default sorting order for the number is ascending order
# default sorting order for string is alphabetical order
# we should know that list should contain homogenoius data otherwise we will get typirder
# python 2 first sort numb that string follows

#------------------------------------------------------------------------------------------
# math = 50
# phy = 50
# eng = 40
# print(id(math)) # returns Adress
# print(id(phy))
# print(id(eng))
# whenerver we assign a same value to diff variBLES python is going to use same no . 
# aggain it is not going to assign different/seperate  memmorey for the same no. it is going to use same no.

#------------------------------------------------------------------------------------------
# mylist = [50, 22 , 11, 60, 3 , 89, 77]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))
# python uses same array dont creaates another memorey for same array going to give same id array

#------------------------------------------------------------------------------------------
# Membership operator = 1. in    2.  not in
# name = "Prashant"
# print("z" in name)
# print("z" not in name)

#------------------------------------------------------------------------------------------
# for i in range(2,20,3): # (starting point , range , kitne se increment)
#     print(i)
# #i = 3

#------------------------------------------------------------------------------------------
# for i in range(5,0,-1):
#     print(i)

#------------------------------------------------------------------------------------------
# for i in range(1,11):
#     print(i*2," ",i*3," ",i*4," ",i*5," ",i*6," ",i*7," ",i*8," ",i*9," ",i*10)

#------------------------------------------------------------------------------------------

# Wap to accept any digit and check that its pos , neg or zero
# num = int(input("Enter any number : "))
# if num > 0:
#     print("Number is positive")
# if num < 0:
#     print("Number is negative")
# if num == 0:
#     print("Number is zero")

#------------------------------------------------------------------------------------------

# WAP to enetr the days and check the working days and weekend
# days= input("Enter Name of Day:")
# if days == "SATURDAY" or "SUNDAY" or "saturday" or "sunday":
#     print("Weekend")
# else:
#     print("Working Day")

#------------------------------------------------------------------------------------------

# WAP to accept three paper marks and calculate total, percentage ,
# and if percentage is greater than equal to 60 then he/ she is eligible for placement

# math = int(input("Enter marks of math : "))
# phy = int(input("Enter marks of phy : "))
# eng = int(input("Enter marks of eng : "))
# total = math + phy + eng
# print("Total marks : ", total)
# percentage = total / 3
# print("Percentage : ", percentage)
# if percentage >= 60:
#     print("Eligible for placement")
# else:
#     print("Not eligible for placement")

#------------------------------------------------------------------------------------------

# WAP to accept 5 digfferent values in 5 different var and 
#check max value and print by using "Simple if statement"

# a = int(input("Enter 1st value :-  "))
# b = int(input("Enter 2nd value :-  "))
# c = int(input("Enter 3rd value :-  "))
# d = int(input("Enter 4th value :-  "))
# e = int(input("Enter 5th value :-  "))

# if a>b and a>c and a>d and a>e:
#     print("a is Max")
# if b>a and b>c and b>d and b>e:
#     print("b is Max")
# if c>a and c>b and c>d and c>e:
#     print("c is Max")
# if d>a and d>c and d>b and d>e:
#     print("d is Max")
# if e>a and e>c and e>d and e>b:
#     print("e is Max")

#------------------------------------------------------------------------------------------

# # Program to accept three paper marks and find maximum using nested if-else

# p1 = int(input("Enter marks of paper 1: "))
# p2 = int(input("Enter marks of paper 2: "))
# p3 = int(input("Enter marks of paper 3: "))

# # checking which paper has highest marks
# if p1 > p2:
#     if p1 > p3:
#         print("p1 is max")
#     else:
#         print("p3 is max")
# else:
#     if p2 > p3:
#         print("p2 is max")
#     else:
#         print("p3 is max")

#------------------------------------------------------------------------------------------

# WAP to accept percentage and if per
# per = int(input("Enter percentage : "))
# if per >= 90:
#     print("Grade A")
# elif per >= 80 and per < 90:
#     print("Grade B")
# elif per >= 70 and per < 80:
#     print("Grade C")
# else:
#     print("Fail")
#------------------------------------------------------------------------------------------

# indexing and slising are not possible in divtonary {key:value}
# mydict = {
#     "name" : "Ashay",
#     "Professional" : "Developer",
#     "empid" : 1001
# }
# print(mydict)
# print(type(mydict))

# mydict = {  
#     101: "Ashay",
#     102: "Ashish",
#     "103": "Satyarth",
#     "104": "trivani",
#     101: "Ashish",
#     104: "Ashish"
#     }
# print(mydict)

#with the help of key we can access the value
# a = mydict[102]
# print(a)

#we will replace old value by new value
# mydict[102]="Vedant"
# print(mydict)

# only print key x = 0,1
# for x in mydict:
#     print(x)

# only print values
# for x in mydict.values():
#     print(x)

# printing key and values both
# for x,y in mydict.items():
#     print(x,y)

# mydict["Mobile-no"] = 9529432392
# print(mydict)

# mydict = {
#     "name" : "Ashay",
#     "Professional" : "Developer",
#     "empid" : 1001
# }
# mydict.pop(1001)
# print(mydict)


# name = "Ashay Bodhane"
# #indexing = 012345678910
# print(name[0])
# print(name[1])
# print(name[-1])
# #print(name[15]) error index out of bound
# print(name[0:5])
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[::-1])

#------------------------------------------------------------------------------------------
# s = "help4code is a best platfrom for practicing programming"
# print(s.find("help4code"))
# print(s.find("python"))
# print(s.find("programming"))


# s = "prashant" , "ashish" , "sandip"
# m = '|'.join(s)
# print(m)

# s = "Python is a high level programming language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# _____________________________________________________________________________
# print("subject marks: ")
# phy = 50
# chem =60
# math =70
# print("physics={} chemistry={} math={}".format(phy, chem, math))
# print("physics={0} chemistry={1} math={2}".format(phy, chem, math))
# print("physics={x} chemistry={y} math={z}".format(x=phy, y=chem, z=math))
# total = phy + chem + math
# print("Total marks",f"{total}")
# print("Roll no=", "7".zfill(4))
# _____________________________________________________________________________
# print('prashantjha777'.isalnum())   # True
# print('prashantjha'.isalpha())      # True
# print('777f'.isdigit())
# print('sdsdsdsd'.islower())
# print(''.islower())
# print('PRASHANT'.isupper())
# print('My Name Is Prashant'.istitle())
# print(''.istitle())
# print(' '.isspace())
# print("Hello".startswith("He"))
# print("Hello".endswith("lo"))
# _____________________________________________________________________________


# a = 50
# b = 30
# c = 20
# d = 10

# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)


# x = ['A', 'B', 'C', 'D', 'E']
# y = ['A', 'B', 'C', 'D', 'E']
# Z = [1, 2, 3, 4, 5]
# print(x == y) # True
# print(x == Z)
# print(x != Z)

# name = "Ashay Bodhane"
# for i in name:
#     print(i)

# name = "Ashay Bodhane"
# data = ['a','e','i','o','u']
# vowel = 0
# consonant = 0
# for i in name:
#     if i in data:
#         vowel = vowel + 1
#     else:
#         consonant = consonant + 1
# print("Vowel : ", vowel)
# print("Consonant : ", consonant)


# n=int(input("ENTER NUMBER : "))#N=10
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
#     print("THE SUM of first", n, "numbers =", sum)


# name="Ashay"
# newname=""
# for i in name:
#     newname +=i
# print(name)    
# print(newname)         


# mycart=[10,20,200,300,800,60,700]
# for i in mycart:
#     if i>400:
#         print("THIS IS PUCRCHASED CART ITEM:")
#     continue
# print(i)


#WAP to check String is palindrome or not

# # name="racecar"
# name = input
# if name == name[::-1]:
#      print("String is palindrome")
# else:  
#      print("String is not palindrome")



#check for ANAGRAMS

char1 = input("Enter first string : ")
char2 = input("Enter second string : ")     
if sorted(char1) == sorted(char2):
    print("Strings are anagrams")   