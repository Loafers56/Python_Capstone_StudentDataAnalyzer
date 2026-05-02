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
