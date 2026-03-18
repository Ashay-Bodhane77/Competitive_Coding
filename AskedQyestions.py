# import re
# var = 'gasgg54@vscsd!S*'
# count=0
# for i in var:
#     # z = re.search(r'[a-z,o-9]',i)
#     z =ord(i)
#     #print(z)
#     if (z>=97 and z<=122):
#         continue
#     elif z>=48 and z<=57:
#         continue
#     else:
#         count+=1
# print(count)



# #2]
# A=[1,2,3]
# B=[2,3,4]
# C=[3,4,5]
# for i in A:
#     if i in B and i in C:
#         print(i)
        

#3]Move zeroes to the end
 
# list =[1,2,3,12]
# for i in list :
#     if i==0:
#         list.remove(i)
#         list.append(i)
# print(list)        


# #4]Find Second largest number in the list   
# list = [1, 2, 3, 4, 5]
# list.sort()
# print(list)
# print(list[-2])



#5 
N=int(input())
sum=0
mylist=[]
for i in range(N):
    a= int(input("Enter the number: "))
    mylist.append(a)
for j in range(len(mylist)):
    sum+=abs(mylist[j]-mylist[j])
    print(sum)