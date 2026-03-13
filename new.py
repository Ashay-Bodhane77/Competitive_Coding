# name = input("Enter your name: ")
# print("Hello", name)



# #Check a String is palindrome or not
# name = input("Enter a string: ")
# if name == name[::-1]:
#      print("String is palindrome")
# else:  
#      print("String is not palindrome")

#Anagrams

# char1 = input("Enter first string : ")
# char2 = input("Enter second string : ")     
# if sorted(char1) == sorted(char2):
#     print("Strings are anagrams")   

#Add key value pairs to a dictionary

# my_dict = {}  
# my_dict["key1"] = "value1"
# my_dict["key2"] = "value2"
# print(my_dict)


# # CHCK IF A KEY EXISTS IN A DICTIONARY
# my_dict = {"name": "Ashay", "age": "20"}
# key_to_check = "name" 
# if key_to_check in my_dict:
#      print("Key exists in the dictionary")
# else:
    # print("Key does not exist in the dictionary")


#  #ITERAATE OVER DICTIONARY KEYS AND VAKUES
# my_dict = {"name": "Ashay", "age": "20"}
# for key, value in my_dict.items():
#     print("Key:", key, "Value:", value)   

# #NESTED FOR LOOP

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i,end="") 
#         print()


# n=int(input("ENTER NUMBER : "))#N=5
# for i in range(1, n+1):#i=1,2,3,4,5
#     for j in range(1, n+1):#j=1,2,3,4,5
#         print(chr(64+i), end="")#ASCII VALUE OF A=65, B=66, C=67
#     print()


# n=int(input("ENTER NUMBER : "))#N=5
# for i in range(1, n+1):#i=1,2,3,4,5
#     for j in range(1, n+1):#j=1,2,3,4,5
#         print(n+1-i, end="")
#     print()

n=int(input("ENTER NUMBER OF ROWS : "))
for i in range(1, n+1):
    for j in range(1, n+2-1):
        print("*", end="")
    print()