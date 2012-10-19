class Person:
    def __init__ (self, name, isMale):
        self.name=name
        self.isMale=isMale

        if (isMale==True):
            self.sex="Male"
        else:
            self.sex="Female"
    def Show(self):
        print("%s is %s"%(self.name, self.sex))

ShowPerson=[]
info=Person("John", True)
ShowPerson.append(info)
     
info=Person("Maricar", False)
ShowPerson.append(info)

info=Person("Joy", False)
ShowPerson.append(info)

info=Person("Johnny", True)
ShowPerson.append(info)

info=Person("Elvira", False)
ShowPerson.append(info)

for info in ShowPerson:
    info.Show()
