class Person:
    def __init__(self):
        self.Name=""
        self.Sex=""
        self.Age=0

    def Show(self):
        if self.Sex=="Male":
            pronoun="Mr."
        else:
            pronoun="Ms."
        print("%s %s is %i years old."%(pronoun, self.Name, self.Age))

Person1=Person()
Person1.Name="John"
Person1.Sex="Male"
Person1.Age=19

Person2=Person()
Person2.Name="Elvira"
Person2.Sex="Female"
Person2.Age=22

Person1.Show()
Person2.Show()
        
