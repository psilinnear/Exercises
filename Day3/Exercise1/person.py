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

class Student(Pet):
    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats
        def chasesCats(self):
            return self.chases_cats