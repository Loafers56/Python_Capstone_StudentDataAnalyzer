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


class Student:
    def __init__(self, name, grades, grade_level):
        self.name = name
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
    
    # Returns the average as a letter grade
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


# Asks for student information
def student_info():
    # Asks how many students are in a class
    students = int(input("How many students are in your class: "))
    
    # List for the Student objects
    student_data = []
    
    # Loop runs for each student
    for i in range(students):
        # Asks for the name of a student
        name = input(f"Enter the name of your student #{i +1}: ")
        
        
        grade_level = ""
        # Ends the loop if a high school grade level (9-12) is chosen continues the loop if one is not choosen
        while grade_level not in ("9", "10", "11", "12"):
            grade_level = input("What grade is this student in (9-12): ")
            
            if grade_level in ("9", "10", "11", "12"):
                grade_level = grade_level

            else:
                print("Invalid Choice. Use high school grade levels")
        grades = []
    
        # Asks how many grades you want to put in for a student    
        num_grades = int(input(f"How many grades for {name}:"))
        for j in range(num_grades):
            grade = float(input("Enter grade: "))
            grades.append(grade)
    
        # Attachs the data to the Student class
        student = Student(name, grades, grade_level)
        
        # Adds the student data to the student_data list
        student_data.append(student)
    
    return student_data


# In[4]:


# Puts the averages of all student into a list
def average_list(students):
    average_list = []
    for student in students:
        average_list.append(student.average_letter())
        print("")
    return average_list

# Puts the averages of individual students into different lists based on their grade
# Used for the bar chart
def find_grade_level(students):
    grade_9 = []
    grade_10 = []
    grade_11 = []
    grade_12 = []
    # Runs the loop for each student
    for student in students:
        # Checks what grade the student is in
        # Appends their average into their grade level list
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
# Used for the pie chart
def count_average_letter(letters):
    return [
        letters.count("A"),
        letters.count("B"),
        letters.count("C"),
        letters.count("F")
    ]
#
def histo_data(students):
    # Calculates the data needed for the histogram
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


# In[5]:


# Creates a pie chart using the data from histo_data()
def pie_chart(data):
    letter = ['A', 'B', 'C', 'F']

    fig = plt.figure(figsize = (10, 7))
    plt.pie(data, labels=letter)
    plt.title("Total Letter Grade averages off all Students")
    plt.savefig("pie_chart.png")
    plt.show()

# Creates a bar chart using the data from histo_data()
def bar_chart(averages):
    fig, ax = plt.subplots()

    grade_levels = ['9', '10', '11', '12']
    counts = list(averages.values())
    bar_colors = ['tab:green', 'tab:purple', 'tab:red', 'tab:orange']
    ax.bar(grade_levels, counts, color = bar_colors )
    ax.set_ylabel('Averages')
    ax.set_title('Averages of different grade levels')
    plt.savefig('bar_chart.png')
    plt.show()


# In[12]:


# Asks the user if they want a histogram
def ask_for_histogram(letter_list, averages):
    chart = ""
    while chart not in ("none", "neither"):    
        chart = input("Do you want a pie chart (pie), a bar chart(bar), or neither(none)?:").lower()      
        
        if chart == "pie":
            # Prints how many A's, B's, C's, or F's there are
            print(letter_list)
            pie_chart(letter_list)          
        
        elif chart == "bar":
            
            # Prints the average of each class
            print(averages)
            bar_chart(averages)
        
        elif chart in ("none", "neither"):
            print("")
        
        else:
            print("Invalid Choice")

# Asks users if they want to add extra students
def add_extra_students(students):
    update = ""
    while update != "no":
        update = input("Are you sure you want to add more sutdents? (yes/no):").lower()
        
        if update == "yes":
            new_students = student_info()
            
            # Adds the new student into students which is a list 
            students += new_students
            
            # Prints the student list with the new students
            print("\n----Updated Student List----")
            for student in students:
                print(student.show_data(), "\n")
        
        elif update == "no":
            print("")
        
        else:
            print("Invalid Choice")
    
    return students

# Asks the users if they want to save the info to a file
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


# In[13]:


def main():
    students = student_info()

    print("\n----Student List----")
    for student in students:
        print(student.show_data(), "\n")

    average, letter_list, grades, average_grade_level = histo_data(students)
    

    choice = ""
    while choice != "none":
        choice = input("Do you want to see a histogram, add student info (add),save this information to a file (save), or none:").lower()
        print("")
        if choice == "histogram":
            ask_for_histogram(letter_list, average_grade_level)
        
        elif choice == "add":
            students = add_extra_students(students)
            
            # Updates the data that is already saved in these variables
            # So this new data can be used for the histogram
            average, letter_list, grades, average_grade_level = histo_data(students)

        elif choice == "save":
            save_to_file(students)
            print("Saved")
        
        elif choice == "none":
            print("Have a good day!")
            break
        
        else:
            print("Invalid Choice")           


# In[10]:


main()


# In[ ]:




