class Person:
    def __init__(self, Name, Sex, Age):
        self.Name=Name
        self.Sex=Sex
        self.Age=Age

    def Show(self):
        if self.Sex=="Male":
            pronoun="Mr."
        else:
            pronoun="Ms."
        print("%s %s is %i years old."%(pronoun, self.Name, self.Age))

Person1=Person("John", "Male", 19)
Person2=Person("Sony", "Male", 27)
Person3=Person("Elvira","Female",22)
Person4=Person("Ondoy","Female",20)
Person5=Person("Jhane","Female",17)
Person6=Person("Joy","Female",19)
Person7=Person("Ferdinand","Male",17)
Person8=Person("Gabriel","Male",19)

Person1.Show()
Person2.Show()
Person3.Show()
Person4.Show()
Person5.Show()
Person6.Show()
Person7.Show()
Person8.Show()
        
