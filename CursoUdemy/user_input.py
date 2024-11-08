
# use input
def weather_temperature(a):
    if a > 7:
        return "warm"
    else:
        return "Cold"
    
user= float(input("Enter temperature:"))
print(weather_temperature(user))

# string formatting in some forms

user_input = input("Enter your name:")
message = "Hello %s!" % user_input
other_message = f"Hello {user_input}!"
print(message)
print(other_message)

#String Formatting with Multiple Variables
name = input("Enter your name: ")
surname = input("Enter your surname: ")

all_message = f"Hello, {name} {surname}!"
all_other_message = "Hello %s %s!" % (name, surname)
print(all_other_message)
print(all_message)

#There is also another way to format strings using the "{}".format(variable) form. Here is an example:

name = "John"
surname = "Smith"
 
message = "Your name is {}. Your surname is {}".format(name, surname)
print(message)
#Output: Your name is John. Your surname is Smith



#In this section, you learned that:

#A Python program can get user input via the input function:

#The input function halts the execution of the program and gets text input from the user:

name = input("Enter your name: ")


#The input function converts any input to a string, but you can convert it back to int or float:

experience_months = input("Enter your experience in months: ")
experience_years = int(experience_months) / 12


#You can also format strings with:

name = "Sim"
experience_years = 1.5
print("Hi {}, you have {} years of experience".format(name, experience_years))
#Output: Hi Sim, you have 1.5 years of experience.