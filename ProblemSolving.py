# def msg(): #called from main.py
#     print("Hello World")
# msg()


# def add(): #called function
#     n1 = int(input("Enter first number: "))
#     n2 = int(input("Enter second number: "))
#     print("The sum is:", n1 + n2)
# add()    



# def arithemmtic(): #called function
#     n1 = int(input("Enter first number: "))
#     n2 = int(input("Enter second number: "))
#     print("The sum is:", n1 + n2)
#     sum = n1+n2
#     mul = n1*n2
#     div = n1/n2
#     sub = n1-n2
#     return sum, mul, div, sub
# result = arithemmtic()    
# print(result)


#4
#i] Positional Arguments
#ii] Keyword Arguments
#iii] Default Arguments
#iv] Variable Length Arguments


# #1] Posiotobal Arguments
# def personalInfo(fname,lname):
#     print("First Name:", fname)
#     print("Last Name:", lname)

# fname ="Ashay" 
# lname = "Bodhane"   
# personalInfo(fname,lname) #positional arguments


# # #2] Keyword Arguments
# def cityName(city="Nagpur"):
#     print("City:", city)

# cityName("Pune") #keyword 
# cityName("Mumbai")
# cityName()


# # VARIABLE LENGTH ARGUMENTS
# def studentNames(*names):
    
#         print(names)

# studentNames("Ashay","Aryan","Vedant","prathmesh")



#SEARCH THE ELEMENT 7 IN LISY
mylist = [1,2,3,4,5,6,7,8,9]

def searchElement(target):
    for i in range(len(mylist)):
        if target == mylist[i]:
            print("Element found at index:", i)
    else:   
       print("Element not found in the list")        
   
searchElement(0)        
      