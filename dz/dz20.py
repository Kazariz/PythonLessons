class Human:
    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age

    def __str__(self):
        return f"Человек: {self.full_name}, Возраст: {self.age}"


class Student(Human):
    def __init__(self, full_name, age, speciality, group, year):
        super().__init__(full_name, age)
        self.speciality = speciality
        self.group = group
        self.year = year

    def __str__(self):
        return (f"Студент: {self.full_name}, Возраст: {self.age}, "
                f"Специальность: {self.speciality}, Группа: {self.group}, Курс: {self.year}")


class Graduate(Student):
    def __init__(self, full_name, age, speciality, group, year, diploma_topic):
        super().__init__(full_name, age, speciality, group, year)
        self.diploma_topic = diploma_topic

    def __str__(self):
        return (f"Дипломник: {self.full_name}, Возраст: {self.age}, "
                f"Специальность: {self.speciality}, Группа: {self.group}, "
                f"Курс: {self.year}, Тема: {self.diploma_topic}")


class Teacher(Human):
    def __init__(self, full_name, age, subject, experience):
        super().__init__(full_name, age)
        self.subject = subject
        self.experience = experience

    def __str__(self):
        return (f"Преподаватель: {self.full_name}, Возраст: {self.age}, "
                f"Предмет: {self.subject}, Стаж: {self.experience}")


def parse_line(line):
    words = line.split()
    if len(words) < 4:
        return Human(" ".join(words[:2]), int(words[2]))

    try:
        age = int(words[2])
        experience = int(words[-1])
        subject = " ".join(words[3:-1])
        return Teacher(f"{words[0]} {words[1]}", age, subject, experience)
    except:
        pass

    try:
        age = int(words[2])
        year = int(words[5])
        speciality = words[3]
        group = words[4]
        if len(words) > 6:
            diploma_topic = " ".join(words[6:])
            return Graduate(f"{words[0]} {words[1]}", age, speciality, group, year, diploma_topic)
        else:
            return Student(f"{words[0]} {words[1]}", age, speciality, group, year)
    except:
        pass

    try:
        return Human(f"{words[0]} {words[1]}", int(words[2]))
    except:
        return Human(line, 0)


data = [
    "Батадалаев Даши 16 ГК Web_011 5",
    "Загидуллин Линар 32 РПО PD_011 5",
    "Шугани Сергей 15 РПО PD_011 5 Защита персональных данных",
    "Данышин Андрей 38 Астрофизика 110",
    "Маркин Даниил 17 ГК Python_011 5",
    "Башкиров Алексей 45 Разработка приложений 20"
]

people = [parse_line(line) for line in data]

for person in people:
    print(person)
