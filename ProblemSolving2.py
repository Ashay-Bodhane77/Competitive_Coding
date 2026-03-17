# fruit_list1 = ["apple", "Berry", "cherry", "Papaya"] 
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] = "Guava"
# fruit_list3[1] = "Kiwi"

# sum = 0
# for i in (fruit_list1, fruit_list2, fruit_list3):
#     if i[0] == "Guava":
#         sum += 1    
#     if i[1] == "Kiwi":
#         sum += 20
# print(sum)        




# #2]
# def f(i,values = []):
#     values.append(i)
#     print(values)
#     #return valuees

# f(1)#called function
# f(2)
# f(3)



# #3]
# def func(value,values):
#     var=1
#     values[0] = 44
# t = 3
# v = [1,2,3]
# func(t,v)
# print(t,v[0])




#4]
# dict = {'c': '97', 'a': '96','b':'98'}
# for _ in sorted(dict):
#     print(dict[_])



# #5]
# from operator import index

# fruit = {}
# def addone(index):
#     if index in fruit:
#       fruit[index] += 1
#     else:
#       fruit[index] = 1    
# addone('apple')
# addone('banana')
# addone('apple')
# print (len(fruit))



#6] PRODUCT OF ARRAY EXCEPT SELF :
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]
    
        return output        