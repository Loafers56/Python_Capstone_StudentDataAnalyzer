#!/usr/bin/env python
# coding: utf-8

# # The program analyzes student data
# # This program allows the user to input student data
# # It stores the students as objects and is able to keep track of their grade

# In[1]:


# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


# In[2]:


class StudentBase:
    def __init__(self, name):
        self.name = name
    
    # Displays the students name    
    def display(self):
        return self.name

    # Shows all of a students data
    def show_data(self):
        data = (
        f"Student: {self.name}\n"
        f"Grade level: {self.grade_level}\n"
        f"Grades: {self.grades}\n"
        f"Average: {self.average()}\n"
        f"Highest grade: {self.highest_score()}\n"
        f"Lowest grade: {self.lowest_score()}\n"
        f"Letter grades: {self.number_to_letter()}\n"
        )
        return data


# In[3]:


class Student(StudentBase):
    def __init__(self, name, grades, grade_level):
        super().__init__(name)
        self.grades = grades
        self.grade_level = grade_level
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


# In[28]:


def student_info():
    students = int(input("How many students are in your class: "))
    student_data = []
    for i in range(students):
        # Asks for the name of a student
        name = input(f"Enter the name of your student #{i +1}: ")
        
        grade_level = ""
        while grade_level not in ("9", "10", "11", "12"):
            grade_level = input("What grade is this student in: ")
            
            if grade_level in ("9", "10", "11", "12"):
                grade_level = grade_level

            else:
                print("Invalid Choice")
        grades = []
    
        # Asks how many grades you want to put in for a student    
        num_grades = int(input(f"How many grades for {name}:"))
        for j in range(num_grades):
            grade = float(input("Enter grade: "))
            grades.append(grade)
    
        # Attachs the data to the Student class
        student = Student(name, grades, grade_level)
        student_data.append(student)
    
    return student_data


# In[19]:


# Puts the averages of all student info a list
def average_list(students):
    average_list = []
    for student in students:
        average_list.append(student.average_letter())
        print("")
    return average_list

# Puts the averages of individual students into different lists based on their grade
def find_grade_level(students):
    grade_9 = []
    grade_10 = []
    grade_11 = []
    grade_12 = []
    for student in students:
        grade_level = student.grade_level
        if grade_level == '9':
            grade_9.append(int(student.average()))
        elif grade_level == '10':
            grade_10.append(int(student.average()))
        elif grade_level == '11':
            grade_11.append(int(student.average()))
        elif grade_level == '12':
            grade_12.append(int(student.average()))
        else:
            print("Invalid grade level")
   
    return {"Grade_9": grade_9, "Grade_10": grade_10,"Grade_11": grade_11, "Grade_12": grade_12}

# Counts how many students average is a A, B, etc.
def count_average_letter(letters):
    return [
        letters.count("A"),
        letters.count("B"),
        letters.count("C"),
        letters.count("F")
    ]

def pie_chart(data):
    letter = ['A', 'B', 'C', 'F']

    fig = plt.figure(figsize = (10, 7))
    plt.pie(data, labels=letter)
    plt.title("Total Letter Grade averages off all Students")
    plt.savefig("pie_chart.png")
    plt.show()


def bar_chart(averages):
    fig, ax = plt.subplots()

    grade_levels = ['9', '10', '11', '12']
    # Values gets all values() from a dictionary and list() converts those values into a list
    # This turns the lists from the dictionary into actual usable lists
    counts = list(averages.values())
    bar_colors = ['tab:green', 'tab:purple', 'tab:red', 'tab:orange']
    ax.bar(grade_levels, counts, color = bar_colors )
    ax.set_ylabel('Averages')
    ax.set_title('Averages of different grade levels')
    plt.savefig('bar_chart.png')
    plt.show()


# In[26]:


def ask_for_histogram(letter_list, averages):
    chart = ""
    while chart not in ("none", "neither"):    
        chart = input("Do you want a pie chart (pie), a bar chart(bar), or neither(none)?:").lower()      
        
        if chart == "pie chart":
            print(letter_list)
            pie_chart(letter_list)          
        
        elif chart == "bar chart":
            print(averages)
            bar_chart(averages)
        
        elif chart in ("none", "neither"):
            print("")
        else:
            print("Invalid Choice")

def update_student_info(students):
    update = ""
    while update != "no":
        update = input("Type yes to add student(s) type no to not:").lower()
        if update == "yes":
            new_students = student_info()
            students += new_students
            print("\n----Updated Student List----")
            for student in students:
                print(student.show_data(), "\n")
        elif update == "no":
            print("")
        else:
            print("Invalid Choice")
    return students

def save_to_file(students):
    file = ""
    while file not in ("no", "yes"):
        file = input("Saving overwrites previous save. Do you still want to save? (yes/no):").lower()
        if file == "yes":
            output_file = open("Student_data.txt", "w")
            output_file.write("----Student Data----\n")
            for student in students:
                output_file.write(f"{student.show_data()} \n")
            output_file.close()
            print("")
        elif file == "no":
            print("")
        else:
            print("Invalid Choice")


# In[22]:


def histo_info(students):
    # Calculates the info needed for the histogram
    average = average_list(students)
    letter_list = count_average_letter(average)
    grades = find_grade_level(students)
   
    # For every grade level and its list of averages calculate the total grade average
    # Else return a 0 
    average_grade_level = {
        grade: (sum(values) / len(values) if values else 0)
        for grade, values in grades.items()
    }
    return average, letter_list, grades, average_grade_level


# In[23]:


def main():
    students = student_info()

    print("\n----Student List----")
    for student in students:
        print(student.show_data(), "\n")

    average, letter_list, grades, average_grade_level = histo_info(students)
    

    choice = ""
    while choice != "none":
        choice = input("Do you want to see a histogram, add student info (add),save this information to a file (save), or none:").lower()
        
        if choice == "histogram":
            ask_for_histogram(letter_list, average_grade_level)
        
        elif choice == "add":
            students = update_student_info(students)
            average, letter_list, grades, average_grade_level = histo_info(students)

        elif choice == "save":
            save_to_file(students)
            print("Saved")
        
        elif choice == "none":
            break
        
        else:
            print("Invalid Choice")           


# In[24]:


main()


# In[ ]:




