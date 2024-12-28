#info = {
#  "name" : "Anushree",
#   "age" : 19,
#   "class" : ["python", "java", "c++"], 
#   "class" : "cs_finalyr",
#   "marks" : 89,
#   "cgpa" : 9.3,
#}

#null_dict = {}
#print(null_dict)

#info["name"] = "anushreedhomne"
#info["clg"] = "DACN"
#print(info)

#dictionary in python
# student = {
#      "name" : "Anushree Dhomne",
#      "subjects" : {
#          "stats" : 76,
#          "cs" : 90,
#          "math" : 80,
#      }
#  }

#  print(student["subjects"][" cs"])

# print(len(list(student.keys())))

# print(len(list(student.values())))

# print(student.items())
# pairs = list(student.items())
# print(pairs[0])

# print(student.get("name"))
# print(student["name2"])  #error
# print(student.get("name2")) #no error -> none

# student.update({"city" : "nagpur"})
# print(student)

# collection = {1,2,3,4,4,4, "hallo", "world", 5}

# print(len(collection))  #total number of items
# print(type(collection))

# num = set()  
# print(num) 

# collection = set()
# collection.add(0)   #adda an element
# collection.add(1)
# collection.add(2)
# collection.add(2)
# collection.add("Anushree")
# collection.add((7,8,9))

 #collection.remove(1)     #removes an element
# collection.clear()       

#print(collection)

# collection = {"hello", "anushree", "python", "java"}
# print(collection.pop()) 

# set1 = {1,2,3}
# set2 = {3,4,5}

# print(set1.union(set2))    #{1,2,3,4,5}     
# print(set1.intersection(set2))  #{3}

#PQ-1
# dictionary = {
#       "table" : ["a piece of furniture", "list of facts & figures"],
#       "cat" : "a small animal"
#   }
# print(dictionary)

#PQ-2
# subjects = {
#   "python", "java", "c++", "python", "javascript", "java", 
#   "python", "java", "c++", "c"}
# print(len(subjects))

#PQ-3
# marks = {}
# x = int(input("enter stats: "))
# marks.update({"stats" : x})

# y = int(input("enter cs: "))
# marks.update({"cs" : y})

# z = int(input("enter math: "))
# marks.update({"math" : z})

# print(marks)

# PQ-4
values = {9, "9.0"}
print(values)

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)
