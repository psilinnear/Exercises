class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def getName(self):
        return self.name
    def getSpecies(self):
        return self.surname
    def __str__(self):
        return "The student's name is %s %s" % (self.name, self.surname)

class Student(Person):
    def __init__(self, name, surname, subject):
        Person.__init__(self, name, surname)
        self.subject = subject
        def subject(self):
            return self.subject
        def __str__(self):
            return "The subject is %s %s %s" % (self.name, self.surname, self.subject)