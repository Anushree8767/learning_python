# def calc_sum(a, b):
#     sum = a + b 
#     return sum
#     print(sum)

# calc_sum(2, 4) 
 
# def calc_sum(a, b):
#     return a + b

#     sum = calc_sum(1,3)
#     print(sum)

# def print_hello():
#     print("hello")

# print_hello()

#average of 3 no.

# def calc_avg(a,b,c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg
# calc_avg(1,5,6)

# def cal_prod(a=1,b=5):
#     print(a*b)
#     return a*b

# cal_prod()

#pq-1
# cars = ["BMW","tesla","porche","corvette"] 
# cities = ["nagpur", "delhi","mumbai"]

# # print(cities[0], end=" ")
# # print(cities[1])

# def print_len(cars):
#     print(len(list))

#     print_len(cars)
#     print_len(cities)

# n = 5

# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#         print(fact)

#         cal_fact(5)

#con USD to INR
# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val, "USD =", inr_val, "INR")

# converter(56)
    
#even or odd
# n = 4
# def cal_num(n):
#     if(n%2==0):
#         print("EVEN")
#     else:
#         print("ODD")

# cal_num(n)


#recursion
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
#     print("END")
# show(5)

#return n!
# def fact(n):
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return fact(n-1) * n
# print(fact(4))

# PQ-1 
# def cal_sum(n):
#     if(n == 0):
#         return 0
#     return cal_sum(n-1) + n
# sum = cal_sum(15)
# print(sum)

#pq-2

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango", "apple", "banana", "grape"]

print_list(fruits)