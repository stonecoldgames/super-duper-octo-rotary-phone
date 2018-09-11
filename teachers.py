import random
class Coder(object):
  def __init__(self,name, languages):
    self.name = name
    self.languages = languages
  

class Teacher(object):
  def __init__(self,name,classes):
    self.name = name
    self.classes = classes
  def Grade(self):
    # vvv private variable vvv
    grades = ["a","b","c","d","f"]
    gradechoice = random.randint(0,len(grades))
    classchoice = random.randint(0,len(self.classes))
    return "You got a {} in {} class.".format(grades[gradechoice-1],self.classes[classchoice-1])
class Artist(object):
  def __init__(self,name,mediums):
    self.name = name
    self.mediums = mediums
  def makeArt(self):
    getmedium = random.randint(0,len(self.mediums)-1)
    return("{} made a work of {} art.".format(self.name,self.mediums[getmedium]))
    
  

# Combining classes vvv
class Ross(Coder,Teacher):
  # vvv constructor vvv
  def __init__(self, name, classes,languages):
    Teacher.__init__(self, name,classes)
    Coder.__init__(self, name,languages)
78
class Carlos(Teacher,Artist):
  def __init__(self,name,classes,mediums):
    Teacher.__init__(self,name,classes)
    Artist.__init__(self,name,mediums)

  def Grade(self):
    grades = ["C","D","F"]
    if random.randint(1,100)%2 == 0:
      mod = "+"
    else:
      mod = "-"
    gradechoice = random.randint(0,len(grades))
    classchoice = random.randint(0,len(self.classes))
    return "You got a {}{} in {} class.".format(grades[gradechoice-1],mod,self.classes[classchoice-1])
class Student(object):
  def __init__(self,name,classes,teachers):
    self.name = name
    self.classes = classes
    self.teachers = teachers
    self.reportcard = []
  def Reportcard(self):
    print ("Your Grades are:")
    for teacher in self.teachers:
      self.reportcard.append(teacher.Grade())
      print(teacher.Grade())







ross= Ross("Ross",["coding","algebra"],["python","opencv"])
carlos = Carlos("Carlos",["studio art","graphic design"],["Oil Paint","Charcoal","Collage"])
daniel = Student("Daniel",["i+d","coding"],[ross,carlos])
print (ross.languages)
print(ross.Grade())
print(carlos.Grade())
print(carlos.makeArt())

daniel.Reportcard()
