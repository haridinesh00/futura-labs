# class person:
#     def __init__(self, name, idNo):
#         self.name = name
#         self.id = idNo
#
#     def display(self):
#         print(self.name)
#         print(self.id)
# a = person("rahul", 564)
# print(a.name)
# print(a.id)


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def display(self):
        print(self.id)
        print(self.name)
class Employee(Person):
    def __init__(self, id, name, salary, post):
        self.salary = salary
        self.post = post
        Person.__init__(self, id, name)
a = Employee("234", "John", 56789, "Developer")
a.display()
