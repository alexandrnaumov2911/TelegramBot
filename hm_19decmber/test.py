class Human:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def say_name(self):
        return f'Меня зовут {self.name}'

    def say_age(self):
        return f'Мой возраст {self.age}'

    def __repr__(self):
        return f'Меня зовут {self.name}, мне {self.age}'

class Student(Human):

    def __init__(self, name:str, age:int, grade:int):
        self.grade = grade
        super().__init__(name, age)

    def say_ready(self):
        return 'Я готов ответить!'

    def say_grade(self):
        return f'Я учусь в {self.grade} классе'

    def __repr__(self):
        return f'Меня зовут {self.name}, мне {self.age}, и я учусь в  {self.grade} классе'

class Teacher(Human):

    def __init__(self, name: str, age: int, teaching_profile: str, teaching_experience: int):
        self.teaching_profile = teaching_profile
        self.teaching_experience = teaching_experience
        super().__init__(name, age)

    def say_teaching_profile(self):
        return f'Я преподаю урок {self.teaching_experience}'

    def say_teaching_experience(self):
        return f'Я работаю учителем уже {self.teaching_experience} лет'

    def __repr__(self):
        return f'Меня зовут {self.name}, мне {self.age}, я преподаю урок - {self.teaching_profile}, я преподаю уже {self.teaching_experience} лет'

class Director(Teacher, Human):

    def __init__(self, name: str, age: int, teaching_profile: str, teaching_experience: int, director_experience: int):
        self.director_experience = director_experience
        super().__init__(name, age, teaching_profile, teaching_experience)

    def say_director_experience(self):
        return f'Я работаю директором уже {self.director_experience}'

    def __repr__(self):
        return f'Меня зовут {self.name}, мне {self.age}, я преподаю урок - {self.teaching_profile}, я преподаю уже {self.teaching_experience} лет, а директором я работаю {self.director_experience} лет'

people1 = Student('Aлександр', 14, 7)
people2 = Teacher('Ольга', 32, 'Английский', 8)
people3 = Director('Николай', 58, 'История', 34, 8)
print(people1)
print(people2)
print(people3)