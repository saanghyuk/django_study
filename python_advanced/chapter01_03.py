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
  tuition_per = 1.0

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
    return 'After tuition -> Id : {}, fee : {}'.format(self._id, self._tuition * Student.tuition_per)

  #Instance Method
  def __str__(self):
    return 'Student Info -> name : {}, grade : {}, email : {}'.format(self.full_name(), self._grade, self._email)

  #Class Method
  #cls라는 첫번째 인자로 Class가 넘어오는 거샹.
  #cls = Student
  @classmethod
  def raise_fee(cls, per):
    if per <= 1 :
      print('Please Enter 1 or More')
      return
    cls.tuition_per = per
    print('Succed! tuition increased!')


#학생 인스턴스
student_1 = Student(1, 'Kim', 'Sarang', 'student1@naver.com', '1', 400, 3.5)
student_2 = Student(1, 'Lee', 'Myungho', 'student2@daum.net', '2', 500, 4.3)

#기본 정보
print(student_1) #str구현해서 확인이 쉬움
print(student_2)
print(student_1.__dict__)
print(student_2.__dict__)

#전체 정보
print(student_1.detail_info())
print(student_2.detail_info())

# 학비 정보(인상 전)
print(student_1.get_fee())
print(student_2.get_fee())
print()

# 학비 인상(클래스 메소드 미사용)
# 직접 접근하는 것? 너무 안좋다고 말했음.
# 실수로 1.2대신 1.3누르면 어쩔꺼야.
Student.tuition_per = 1.2
print(student_1.get_fee_culc())
print(student_2.get_fee_culc())
print()
Student.tuition_per = 1.0 # reset용 code

# 학비 인상(클래스 메소드 사용)
Student.raise_fee(1)
Student.raise_fee(1.5)
print(student_1.get_fee_culc())
print(student_2.get_fee_culc())

