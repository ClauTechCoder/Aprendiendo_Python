student_grades = [9 , "Hello" , [1, 2, 4.33]]
student_grades_true = [9.8, 7.7, 4.5]
print(student_grades * 3) # sale la lista repetida 3 veces

student_grades_per_range = list(range(0, 11))
print(student_grades_per_range)

# CALCULATE DE MEAN OF student'S grades
mysum = sum(student_grades_true) # sum values of that list
length = len(student_grades_true)
media = mysum / length
print(media)

# BEST WAY
student_grades_true = [9.8, 7.7, 4.5] # LIST
student_grades_true = {"Marry": 9.8, "sim": 7.7, "John": 4.5} # DICTIONARY
mysum = sum(student_grades_true.values()) #choose only the value of the dictionary
length = len(student_grades_true)
media = mysum / length
print(media)

