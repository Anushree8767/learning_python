#str1 = "This is a string."
#str2 = 'Anushree'
#str3 = """this is a string."""
#str1 = "THis is a string.\nwe are creating it in python."
#print(str1)
#str1 = "heyy"
#len1 = len(str1)
#print(len1)

#str2 = "bro"
#len2 = len(str2)
#print(len2)
#final_str = str1 + " " + str2
#print(final_str)
#print(len(final_str))

#str = "Anushree"
#print(str[1])

#str = "Anushree"
#print(str[:4]) #[0:4]
#print(str[5:]) #[5:len(str)]
#print(str[-8:-1])

#str = "Studying python from youtube"
#print(str.endswith("ube")) #returns True if string ends with substr
#print(str.capitalize()) #Capitalize first char
#str = str.capitalize()
#print(str)
#print(str.replace("o","a")) #replace all occurance of old to new
#print(str.find("python")) #return 1st index of 1st occurrer
#print(str.count("o"))

#PQ-1
#name = input("Enter name: ")
#len1 = len(name)
#print(len1)

#PQ-2
#str = "hey i want $15 and $18 for ..."
#print(str.count("$"))

#Conditional Statements

#age = 21
#if(age >= 18):
#    print("can vote")
#    print("can drive")

#light = "green"

#if(light == "red"):
#    print("stop")
#elif(light == "green"):
#    print("go")
#elif(light == "yellow"):
#    print("Wait")
#else:
#    print("light is broken")

#num = 5
#if(num > 2):
#    print("greater than 2")
#    if(num > 3):
#        print("greater than 3")

#marks = int(input("enter student marks"))

#if(marks >= 90):
#    grade = "A"
#elif(marks >= 80 and marks < 90):
#    grade = "B"
#elif(marks >= 70 and marks < 80):
#    grade = "C"
#elif(marks >= 60 and marks <70):
#    grade = "D"
#else:
#    grade = "F"
#print("grade of the student is ", grade)

#nesting
age = 87

if(age >= 18):
    if(age >= 80):
        print("Cannot drive")
    else:
        print("can drive") 
else:
    print("cannot drive") 
