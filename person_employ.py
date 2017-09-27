# class 상속 예제

# 부모 class 작성
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def about_me(self):
        print("저의 이름은 %s 이고, 저의 나이는 %s 입니다. 저는 %s 입니다" % (self.name, self.age, self.gender))


# 상속 class
class Employee(Person):
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name,age,gender)
        self.salary = salary
        self.hire_date = hire_date

    def do_work(self):
        print("열심히 일을 하겠습니다")

    def about_me(self):
        super().about_me()
        print("제 급여는 %s, 제 채용일은 %s 입니다." % (self.salary, self.hire_date))
    
myperson = Person("David", "29", "male")
employee = Employee("David", "29", "male", "200000$", "1990/10/18")
myperson.about_me()
employee.about_me()
