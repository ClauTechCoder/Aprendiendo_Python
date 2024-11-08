# mean with difference between list, dictionaries....

def mean_with_check(value):
    if type(value) == dict:
        the_mean = sum(value.values())/len(value)
    else:
        the_mean = sum(value)/len(value)
    
    return the_mean

student_grades = {"Marry": 9.2,"Sim": 8.8,"John":7.5}
student_grades_list = [8.8,9.1,7.7]

print(mean_with_check(student_grades))

print(mean_with_check(student_grades_list))


#So far, you learned how to check for one single condition:

x = 1
 
if x == 1:
    print("Yes")
else:
    print("No")


#You can also check if two conditions are met at the same time using an and operator:

x = 1
y = 1
 
if x == 1 and y==1:
    print("Yes")
else:
    print("No")
#That will return Yes since x == 1 and y ==1 are both True.



#You can also check if one of two conditions are met using an or operator:

x = 1
y = 1
 
if x == 1 or y==2:
    print("Yes")
else:
    print("No")
#That will return Yes since at least one of the conditions is True. In this case x == 1 is True.

# my own exercise
#Define a function that:
#(1) takes a temperature as a parameter
#(2) returns "Hot" if the temperature is greater than 25
#(3) returns "Warm" if the temperature is between 15 and 25, including 15 and 25.
#(4) returns "Cold" if the temperature is less than 15.
def my_funcion(temp):
    if temp > 25:
        return "Hot"
    elif 15 <= temp <= 25:
        return "Warm"
    elif temp < 15:
        return "Cold"


Define functions:

def cube_volume(a):
    return a * a * a


Write if-else conditionals:

message = "hello there"
 
if "hello" in message:
    print("hi")
else:
    print("I don't understand")


Write if-elif-else conditionals:

message = "hello there"
 
if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")


Use the and operator to check if both conditions are True at the same time:

x = 1
y = 1
 
if x == 1 and y==1:
    print("Yes")
else:
    print("No")


Use the or operator to check if at least one condition is True:

x = 1
y = 2
 
if x == 1 or y==2:
    print("Yes")
else:
    print("No")


Check if a value is of a particular type with isinstance:

isinstance("abc", str)
isinstance([1, 2, 3], list)
or directly:

type("abc") == str
type([1, 2, 3]) == lst
