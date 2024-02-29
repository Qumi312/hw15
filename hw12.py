class Student:

    def __init__(self, name, subjects_file):
        self.data_subjects_test_score = {}
        self.name = name
        self.data_subjects = {}
        self.subjects = self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):
        with open(subjects_file, encoding='utf-8') as f:
            subjects = f.read()
        return subjects

    def add_grade(self, subject, grade):
        self.data_subjects[subject] = grade

    def add_test_score(self, subject, test_score):
        self.data_subjects_test_score[subject] = test_score

    def get_average_grade(self):
        value = 0
        for i, v in self.data_subjects.items():
            value += v
        return value / len(self.data_subjects)

    def get_average_test_score(self, subject):
        if subject in self.data_subjects:
            return float(self.data_subjects_test_score[subject])
        else:
            raise ValueError('Предмет Биология не найден')
    def __str__(self):
        subjects = ''
        keys = list(self.data_subjects_test_score.keys())
        for key in keys:
            subjects = subjects + ", " + key
        return f'Студент: {self.name}\nПредметы: {subjects[2::]}'
    def __getattr__(self, name):
        if name in self.subjects:
            return self.subjects[name]
        else:
            raise AttributeError(f"Предмет {name} не найден")
    def __setattr__(self, name, value):
        if name == 'name':
            if not value.replace(' ', '').isalpha() or not value.istitle():
                raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        super().__setattr__(name, value)



student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)