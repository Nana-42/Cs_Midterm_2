class Student_Entry():
#consturctor containing student name and id
    def __init__(self, name, sid):
        self.name = name
        self.sid = sid
        self.labs = 0
        self.assignments = 0
        self.midterm = 0
        self.final = 0

#Average of the given student
    def get_average(self):
        return self.labs + self.assignments + (self.midterm * 0.30 + self.final * 0.40)

#Assigning a letter grade to the student
    def letter_grade(self):
        if self.get_average() > 80:
            return "A"
        elif self.get_average() > 70:
            return 'B'
        elif self.get_average() > 60:
            return 'C'
        elif self.get_average() > 50:
            return 'D'
        elif self.get_average() < 50:
            return 'F'
        
    
#printing
bsmith = Student_Entry("Bob Smith", "1000001") 
bsmith.labs = 9.0 
bsmith.assignments = 17.0 
bsmith.midterm = 57.5 
bsmith.final = 60.0 
print(f'Bob Smith: {bsmith.letter_grade()}') 

sjones = Student_Entry("Sally Jones", "1000002") 
sjones.labs = 9.5 
sjones.assignments = 19.5 
sjones.midterm = 81.0 
sjones.final = 74.5 
print(f'Sally Jones: {sjones.letter_grade()}')