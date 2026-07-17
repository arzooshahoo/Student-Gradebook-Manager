class Course:
  def__init__(self, course_code, course_name):
    self.course_code = course_code
    self.course_name = course_name
    self.students = []
    self.assessments = []
  def add_students(self, student_id):
    if student_id not in self.students:
      self.students.append(student_id)

  def find_assessment(self, title):
    for assessment in self.assessment:
      if assessment.title == title:
        return assessment
        return None
        
