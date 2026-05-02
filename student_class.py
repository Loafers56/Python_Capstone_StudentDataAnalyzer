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
