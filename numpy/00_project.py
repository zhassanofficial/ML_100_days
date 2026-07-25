import numpy as np
from numpy import random

'''1. Generate the Data
Suppose you have 10 students and 5 subjects for each student.
Use np.random.randint() to generate marks between 0 and 100'''

marks = np.random.randint(0,101,(10,5))
#print(marks)

'''2. Calculate Statistics
Average marks of each student
Average marks of each Subject
Highest and lowest marks overall'''

average_marks = np.mean(marks , axis=1)  #finding average row wise
average_subject = np.mean(marks , axis=0) # finding average column wise
#print(average_marks) 
#print(average_subject)
higest = np.max(marks)
lowest = np.min(marks)
#print(higest)
#print(lowest)


'''3. Find the Top Student
Find which student has the highest total marks.'''

total_marks = np.sum(marks , axis=1)
top_student = np.argmax(total_marks)  # tells about the index in array 
#print(f"Top student id : {top_student} with total marks {total_marks[top_student]}")

"""4. Grade Students Automatically"""
grades = np.where(average_marks >= 80 , 'A',
                  np.where(average_marks >= 70 , 'B' ,
                           np.where(average_marks >= 60 , 'C',
                                    np.where(average_marks>= 60 , 'D' ,'F'))))

for i in range(len(marks)):
    print(f"studen {i+1} : Average marks {average_marks[i]} with grades{grades[i]}")
