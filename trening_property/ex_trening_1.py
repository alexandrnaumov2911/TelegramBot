class Animal:

    def __init__(self, name:str, age:int, view = 'Dog', owner = None):
        self.name = name
        self._age = age
        self.view = view
        self.owner = owner

    def say_owner(self):
        if self.owner:
            print(f'Мой хозяин {self.owner}')

        else:
            print(f'У меня нет хозяина')
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if self._age == value:
            print('Вы ввели тот же возраст')
        else:
            self._age = value

    def __repr__(self):
        return f'Животное зовут - {self.name}, его возраст - {self.age}, вид животного {self.view}, хозяин - {self.owner}'

animal1 = Animal('Ганс', 17)
animal1.age = 17
animal1.say_owner()
print(animal1)