class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"{self.name} => {self.marks}")

def average_marks(students):
    if not students:
        return 0.0
    total = sum(s.marks for s in students)
    return total / len(students)

if __name__ == '__main__':
    students = [Student('Alice', 80), Student('Bob', 90), Student('Chris', 75)]
    for s in students:
        s.display()
    print('Average:', average_marks(students))
