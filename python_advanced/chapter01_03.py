#Chapter01-02
#파이썬 심화
#클래스 메소드, 인스턴스 메소드, 스테이틱 메소드
#Class Method, Instance Method, Static Method 종류 3가지가 있음.

#기본 인스턴스 메소드
class Student(object):
  '''
  Student Class
  Author : SON
  Date : 2021.03.14
  Description: Class, Static, Instance Method
  '''
  # Class Variable
  tuition = 1.0

  def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
    self._id = id
    self._first_name = first_name
    self._last_name = last_name
    self._email = email
    self._grade = grade
    self._tuition = tuition
    self._gpa = gpa

  # Instance Method
  # Self를 받아서 결과 리턴 하는 것이 인스턴스 메소드
  def full_name(self):
    return '{}, {}'.format(self._first_name, self._last_name)

  #Instance Method
  def detail_info(self):
    return 'Student Detail Info : {}, {}, {}, {}, {}'.format(self._id, self.full_name(), self._email, self._grade, self._tuition, self._gpa)


  #Instance Method
  def get_fee(self):
    return 'Befoore Tuition -> Id : {}, fee : {}'.format(self._id, self._tuition)

  #Instance Method
  def get_fee_culc(self):
    return 'After tuition -> Id : {}, fee : {}'.format(self._id, self._tuition * Student.tuition)



