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


  @classmethod
  # 지금까지는 instnace = Student(a, b, c, d) 이런 방식으로 했지만,
  # 파이썬에서는 아래와 같은 생성자를 classmethod로 만들기를 권고함
  # instance = Student.student_const() 이렇게
  def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
    return cls(id, first_name, last_name, email, grade, tuition*cls.tuition_per, gpa)

  #Static Method
  #유연하고 편함. 클래스 안에, 관련된 함수를 같이 넣어 놓음.
  #cls와 self 둘 다 필요가 없음.
  @staticmethod
  def is_scholarship_st(inst):
    if inst._gpa >= 4.3:
      return '{} is a scholarship recipient.'.format(inst._last_name)
    return 'Sorry. Not a scholarship recipient.'



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
print()


# class method로 생성자 만들어 놓기
# @classmethod
# def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
#   return cls(id, first_name, last_name, email, grade, tuition*cls.tuition_per, gpa)
#클래스 메소드 인스턴스 생성 실습
student_3 = Student.student_const(3, 'Park', 'Minji', 'student3@gmail.com', '3', 550, 4.5)
student_4 = Student.student_const(4, 'Lee', 'Miyoung', 'student4@gmail.com', '4', 600, 4.1)

# 전체 정보
print(student_3.detail_info())
print(student_4.detail_info())
print()


# 학생 학비 변경 확인
# 여기서는 tuition이 아예 학비 인상율 반영되서 variable로 들어가줌.
# 그래서 혼용하거나, class constructor를 씀
print(student_3._tuition)
print(student_4._tuition)
print()
print()

# 장학금 혜택 여부(스테이틱 메소드 미사용)
# 근데 이렇게 하면 함수가 분리되 있잖아.
# cls, self가 없는 뭔가를 누구나 쓸 수 있는 것을 만들어 놓을 순 없을까?
# class와 관계된 것은 그 안에 놓는 것이 좋으니깐.
# 그게 static method
def is_scholarship(inst):
  if inst._gpa >= 4.3:
    return '{} is a scholarship recipient.'.format(inst._last_name)
  return 'Sorry. Not a scholarship recipient.'

print(is_scholarship(student_1))
print(is_scholarship(student_2))
print(is_scholarship(student_3))
print(is_scholarship(student_4))
print()


# 장학금 혜택 여부(스테이틱 메소드 사용)
# 클래스와 인스턴스로 둘다 접근 가능함.
print(Student.is_scholarship_st(student_1))
print(Student.is_scholarship_st(student_2))
print(Student.is_scholarship_st(student_3))
print(Student.is_scholarship_st(student_4))

print(student_1.is_scholarship_st(student_1))
print(student_2.is_scholarship_st(student_2))
print(student_3.is_scholarship_st(student_3))
print(student_4.is_scholarship_st(student_4))





