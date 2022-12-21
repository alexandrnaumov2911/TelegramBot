class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Human):
    def __init__(self, name, age, year_of_study, profile):
        super().__init__(name, age)
        self.year_of_study = year_of_study
        self.profile = profile
class Teacher(Human):
    def __init__(self, name, age, profile, teaching_experience):
        super().__init__(name, age)
        self.teaching_experience = teaching_experience
        self.profile = profile
class Director(Human):
    def __init__(self, name, age, profile, teaching_experience, director_experience):
        super().__init__(name, age)
        self.director_experience = director_experience
        self.profile = profile
        self.teaching_experience = teaching_experience
human1 = Student('Иван', 16, 10, 'informatics')
human2 = Teacher('Ольга', 34, 'informatics', 10)
human3 = Director('Николай', 56, 'history', 32, 10)


