from hw12 import Student
import pytest


@pytest.fixture
def s1():
    return Student("Иван Иванов", "subjects.csv")
@pytest.fixture
def s2():
    return Student('Сидоров Евгений', 'subjects.csv')

def test_init_student(s1):
    assert s1 is not None

def test_incorrect_name():
    with pytest.raises(ValueError):
        Student('евгений 223', 'subjects.csv')

def test_init_incorrect_file():
    with pytest.raises(FileNotFoundError):
        Student('Иван', 'subjects.txt')

def test_incorrect_subject_name():
    with pytest.raises(TypeError):
        Student.get_average_test_score("Биология")





if __name__ == '__main__':
    pytest.main(['-vv'])