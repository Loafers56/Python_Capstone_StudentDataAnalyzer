#!/usr/bin/env python
# coding: utf-8

# # The program analyzes student data
# # This program allows the user to input student data
# # It stores the students as objects and is able to keep track of their grade

# In[1]:


# Import libraries
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


class Class:
    def __init__(self, name):
        self.name = name
        student_data = []
    
    # Displays the students name    
    def display(self):
        return self.name

    # Shows all of a students data
    def show_data(self):
        print(f"Student: {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.average()}")
        print(f"Highest grade: {self.highest_score()}")
        print(f"Lowest grade: {self.lowest_score()}")
        print(f"Letter grades: {self.number_to_letter()}")


# In[3]:


class Student(Class):
    def __init__(self, name, grades):
        super().__init__(name)
        self.grades = grades
    
    # Finds the average of the grades
    def average(self):
        return sum(self.grades)/len(self.grades)
    
    # Finds the highest grade 
    def highest_score(self):
        high = max(self.grades)
        return high
    
    # Finds the lowest grade
    def lowest_score(self):
        low = min(self.grades)
        return low
    
    # Converts the grades into letter grades and puts them into a list
    def number_to_letter(self):
        grades = self.grades
        letter_grades = []
        for grade in grades:
            if grade >= 90:
                letter_grades.append("A")
            elif grade >= 80:
                letter_grades.append("B")
            elif grade >= 70:
                letter_grades.append("C")
            else:
                letter_grades.append("F")
        return letter_grades
    
    def average_letter(self):
        average = self.average()
        letter = []
        letter.append(average)
        for i in letter:
            if i >= 90:
                return "A"
            elif i >= 80:
                return "B"
            elif i >= 70:
                return "C"
            else:
                return "F"


# In[4]:


Bob = Student("Bob", [99, 89, 90, 80])

print(Bob.display())
print(Bob.grades)
print(Bob.average())

print(Bob.highest_score())
print(Bob.number_to_letter())
print(Bob.average_letter())


# In[14]:


def student_info():
    students = int(input("How many students are in your class: "))
    students_names = []
    student_data = []
    for i in range(students):
        # Asks for the name of a student and puts it into a list
        name = input(f"Enter the name of your student #{i +1}: ")
        students_names.append(name)
    
        grades = []
    
        # Asks how many grades you want to put in for a student    
        num_grades = int(input(f"How many grades for {name}:"))
        for j in range(num_grades):
            grade = float(input("Enter grade: "))
            grades.append(grade)
    
        # Attachs the data to the Student class
        student = Student(name, grades)
        student_data.append(student)
    return student_data
students = student_info()

print("\n----Student List----")
for student in students:
    student.show_data()
    print("")

def average_list(students):
    average_list = []
    for student in students:
        average_list.append(student.average_letter())
        print("")
    return average_list
print(average_list(students))


# In[19]:


def count_average_letter():
    letters = average_list(students)
    return [
        letters.count("A"),
        letters.count("B"),
        letters.count("C"),
        letters.count("F")
    ]
print(count_average_letter())

def pie_chart():
    letter = ['A', 'B', 'C', 'F']
    data = count_average_letter()

    fig = plt.figure(figsize = (10, 7))
    plt.pie(data, labels=letter)

    plt.show()
pie_chart()


# In[ ]:


def main():
    students = student_info()

    print("\n----Student List----")
    for student in students:
        student.show_data()
        print("")
    
    average_list(students)
    count
    
    

