# declare a list

monday_temperature = [9.1, 8.8, 7.5]

monday_temperature.append(8.1) # add a new data
print(monday_temperature)


monday_temperature.clear() # empty list now

monday_temperature = [9.1, 8.8, 7.5, 6.6, 9.9]

my_index = monday_temperature.index(8.8) # return positions of that value
print(my_index)

# get a value from the list
my_value_from_list = monday_temperature.__getitem__(1)
my_other_value_from_list = monday_temperature[1]
print(my_value_from_list)
print(my_other_value_from_list) # they are equals methods

# access portions of the list

print(monday_temperature[1:4]) # second to four elemen
print(monday_temperature[1:]) # second to the final
last_item = monday_temperature[-1] # easy
print(last_item)

# now with strings

my_string = 'hello'
print(my_string[1]) # we have e
print(my_string[3:]) # we have lo

temperatures = ['hello', 3.3,6.6]
print(temperatures[0][2:]) # we have the remix and get llo

# now with dictionaries

student_grades = {"emily":9.1, "jack":6.8,"robert": 7.0}

print(student_grades["jack"])

eng_port = {'reain':'chuva','sun':'sol'}
print(eng_port['sun'])

From tuple to list:

>>> cool_tuple = (1, 2, 3)
>>> cool_list = list(cool_tuple)
>>> cool_list
[1, 2, 3]


From list to tuple:

>>> cool_list = [1, 2, 3]
>>> cool_tuple = tuple(cool_list)
>>> cool_tuple
(1, 2, 3)


From string to list:

>>> cool_string = "Hello"
>>> cool_list = list(cool_string)
>>> cool_list
['H', 'e', 'l', 'l', 'o']


From list to string:

>>> cool_list = ['H', 'e', 'l', 'l', 'o']
>>> cool_string = str.join("", cool_list)
>>> cool_string
'Hello'


Lists, strings, and tuples have a positive index system:

["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
   0      1      2      3      4      5      6


And they have a negative index system as well:

["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  -7     -6     -5     -4     -3     -2     -1


In a list, the 2nd, 3rd, and 4th items can be accessed with:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[1:4]
Output: ['Tue', 'Wed', 'Thu']


First three items of a list:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:3]
Output:['Mon', 'Tue', 'Wed'] 


Last three items of a list:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[-3:]
Output: ['Fri', 'Sat', 'Sun']
Everything but the last:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-1] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
Everything but the last two:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-2] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] 


A dictionary value can be accessed using its corresponding dictionary key:

phone_numbers = {"John":"+37682929928","Marry":"+423998200919"}
phone_numbers["Marry"]
Output: '+423998200919'

