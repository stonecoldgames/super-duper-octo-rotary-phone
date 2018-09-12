import random
"""
TODO: 
Implement Time functions
json outs
grading assignments vs entire classes


"""

class Course(object):
  def __init__(self,name,teacher,grade,assignments):
    self.name = name
    self.teacher = teacher
    self.grade = grade
    self.assignments = assignments

class Assignment(object):
  def __init__(self,name,grade,description,duedate):
    self.name = name
    self.grade = grade
    self.description = description
    self.duedate = duedate



class Teacher(object):
  def __init__(self,name,students):
    self.name = name
    self.students = students
    self.courseactions = ["Grade","Assign"]
    self.gradeactions = ["Grade Class","Grade Assignment","Edit Assignment"]
    self.assignmentactions = ["New Assignment","Delete Assignment"]
  def TeacherInterface(self):
    print("Welcome to StoneNet, the world's only straightforward grading system.\nYou are currently in your teacher interface.\nPlease enter the name of the student who's profile you'd like to access below. Type 'list' for a list of your students or type 'exit' to exit.")
    masterin = input(">").lower()
    if masterin == "exit":
      pass # add exit options
    elif masterin == "list":
      print("Your current Students are:")
      for student in self.students:
        print("~"+student.name+"\n")
    else:
      pass
      # figure out a way to go to the student check smoothly
    for student in self.students:
      if masterin == student.name.lower():
        self.StudentInterface(student)
      else:
        print("This student does not exist.")
  def StudentInterface(self,student):
    print ("Welcome to StoneNet, the world's only straightforward grading system.\nYou are currently in {}'s interface.\nPlease enter the name of the Course you'd like to access below or type 'exit' to exit.".format(student.name))
    masterin = input(">").lower()
    if masterin == "exit":
      pass
    for course in student.courses:
      if masterin == course.name:
        if course.teacher == self.name: # put in an else statement that says "you cant do that" if not true
          self.CourseInterface(course,student)
  def CourseInterface(self,course,student):
    print ("Welcome to StoneNet, the world's only straightforward grading system.\nYou are currently in {}'s {} course interface.\nPlease enter the name of the action you'd like to perform below or type 'exit' to exit. For a list of actions, type 'actions'".format(student.name,course.name))
    masterin = input(">").lower()
    if masterin == "exit":
      pass
    elif masterin == "actions":
      print ("Actions available:\n")
      for action in self.actions:
        print("~"+action+"\n")
    elif masterin == "grade":
      GradeInterface(course,student)
    elif masterin == "assign":
      AssignmentInterface(course,student)
  def GradeInterface(self,course,student):
    print ("Welcome to StoneNet, the world's only straightforward grading system.\nYou are currently in {}'s {} grading interface.\nPlease enter the name of the action you'd like to perform below or type 'exit' to exit. For a list of actions, type 'actions'".format(student.name,course.name))
    masterin = input(">").lower()
    if masterin.endswith("class"):
      self.GradeClass()
    if masterin.endswith("assignment"):
      assignmentchoice = input("Which Assignment would you like to grade? for a list of assignments type 'list'.").lower()
      for assignment in course.assignments:
        if assignmentchoice == assignment.name.lower():
          self.GradeAssignment(student,course,assignment)
        # dead end (fix)

    if masterin == "exit":
      pass
    elif masterin == "actions":
      print ("Actions available:\n")
      for action in self.gradeactions:
        print("~"+action+"\n")
    

  
  def AssignmentInterface(self,course,student):
    print ("Welcome to StoneNet, the world's only straightforward grading system.\nYou are currently in {}'s {} assignment interface.\nPlease enter the name of the action you'd like to perform below or type 'exit' to exit. For a list of actions, type 'actions'".format(student.name,course.name))
    if masterin == "exit":
      pass
    elif masterin == "actions":
      for action in self.assignmentactions:
        print("~"+ action +"\n")
    elif masterin.startswith("new"):
    elif masterin.startswith("delete"):
      #delete the Assignment

  def NewAssignment(self,course):
    assignmentname = input("Assignment Name (please no spaces,special characters,etc):")
    #figure out how to make new assignment with unique names etc
    
    
  def GradeCourse(self,student,course):
    gradechoice = input("Letter Grade: ")
    if gradechoice.lower().startswith("a"):
      prep = "an"
    else:
      prep = "a"
    print ("You gave {} {} {} in {} class.".format(student.name,prep,gradechoice,course.name))
    course.grade == gradechoice
    return course.grade          
  def GradeAssignment(self,student,course,assignment):
    gradechoice = input("Letter Grade: ")
    if gradechoice.lower().startswith("a"):
      prep = "an"
    else:
      prep = "a"
    print ("You gave {} {} {} on {} in {} class.".format(student.name,prep,gradechoice,assignment.name,course.name))
    assignment.grade = gradechoice
    return assignment.grade



class Artist(object):
  def __init__(self,name,mediums):
    self.name = name
    self.mediums = mediums
  def makeArt(self):
    getmedium = random.randint(0,len(self.mediums)-1)
    return("{} made a work of {} art.".format(self.name,self.mediums[getmedium]))
    


class Student(object):
  def __init__(self,name,courses):
    self.name = name
    self.courses = courses
    self.reportcard = []
  


compprog = Course("Computer Programming","Ross","No Grade",[])


daniel = Student("Daniel",[compprog])
ross = Teacher("Ross",[daniel])
print (daniel.courses[0].grade)
print (daniel.courses[0].grade)
