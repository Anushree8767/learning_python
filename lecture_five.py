# count = 1
# while count <= 5 :
#     print("hello")
#     count += 1
    
# i = 1   #i = iterator
# while i <= 10:
#     print("hello guys", i)
#     i+=1

# print number from 1 to 5
# i = 1
# while i <= 5:
#     print(i)
#     i +=1

#     print("loop ended")

#from 5 to 1
# i = 50
# while i >= 1:
#         print(i)
#         i -= 1
# print("loop ended")
        
#PQ-1
# n = int(input("enter number :"))
# i = 1
# while i <= 10:
#     print(n*i)
#     i+=1

#PQ-2
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1

#PQ-3

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = 25
# i = 0   #initialization
# while i < len(nums):
#     if(nums[i]==x):
#         print("found at index", i)
#     else:
#         print("finding...")
#     i += 1

#break
# i = 1
# while i<=5:
#     print(i)
#     if(i==3):
#      break
#     i+=1
# print("end of loop")

# i = 0
# while i <= 5:
#     if(i == 3):
#         i += 1
#         continue
#     print(i)
#     i += 1

# veg = ["potato","bringal","ladyfinger","cucumber"]

# for val in veg:
#     print(val)


# tup = (1,2,3,4)

# for val in tup:
#     print(val)

# str = "anushree"

# for char in str:
#      if(char == "n"):
#           print("n found")
#           break
#      print(char)
# else:
#      print("End")

#PQ=1 Using For

# nums = (1,4,9,16,25,36,49,64,81,100)

# x = 81

# idx = 0
# for el in nums:
#     if(el == x):
#         print("number found at idx", idx)
#     idx += 1

#range()

# seq = range(5)

# for i in range(1,7,2):      #range(start, stop, step)
#     print(i)

#PQ USING FOR AND RANGE

# for i in range(100, 0, -1):
#     print(i)

# n = int(input("enter number: "))

# for i in range(1,11):
#     print(n*i)

# for i in range(5):
#     pass

# if i > 5:
#     pass

# print("some usefull work")

# n = 4
# sum = 0
# i = 1
# while i <= n:
#      sum += i
#      i += 1

#      print("total sum =", sum

n = 5
factorial = 1
i = 1
for i in range(i, n+1):
    factorial *= i
    print("factorial=", factorial)