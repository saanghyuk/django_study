
#Chapter01-02
#파이썬 심화
#객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
#클래스 상세 설명
#클래스 변수와 인스턴스 변수

#클래스 재 선언
#실무에서 """첫줄 여기에 클래스 설명 달아줌"""
class Student():
  """
  Student
  Author: SON
  Date : 2021.03.14
  """
  #클래스 변수
  student_count = 0
  """
  Sample __doc__
  """
  def __init__(self, name, number, grade, details, email=None):
    #인스턴스 변수
    self._name = name
    self._number = number
    self._grade = grade
    self._details = details
    self._email = email

    Student.student_count += 1

  def __str__(self):
    return 'str {}'.format(self._name)

  def __repr__(self):
    return 'str {}'.format(self._name)

  def detail_info(self):
    print('Current Id : {}'.format(id(self)))
    print('Student Detail Info: {} {} {}'.format(self._name, self._email, self._details))

  def __del___(self):
    Student.student_count -= 1

#Self 의 의미, 실질적으로 인스턴스화, 붕어빵 기계로 찍어낸 그것
studt1 = Student('Cho', 2, 3, { 'gender' : 'Male', 'score1' : 65, 'score2':44 })
studt2 = Student('Chang', 2, 3, { 'gender':'Female', 'score1':85, 'score2':74 }, 'stu2@naver.com')
#Id값 두개가 서로 다름.
#ID값이 같으면 내부 값들도 같겠지만, Id값이 다르다고 해서 값이 꼭 다른지는 모름.
print(id(studt1))
print(id(studt2))

a = 'ABC'
b = a

# ==는 값을 비교, is 는 ID를 비교
print(studt1==studt2)
print(studt1._name==studt2._name)
print(studt1 is studt2)
print(a is b) # 이러면 True가 나옴.
print(a == b)

# dir & __dict__ 확인
# 실무에서는 dict를 먼저 보고, 없으면 dir을 찾아봄. dict가 훨씬 간단하게 보여줌.
print(dir(studt1))
print(dir(studt2))
print(studt1.__dict__)
print(studt2.__dict__)


# Doctring 주석 출력
# 단 맨 위에 달아놓은 주석만 출력함
print(Student.__doc__)
print()

#실행
studt1.detail_info()
studt2.detail_info()

# 에러
# 아래 함수는 당연히 호출 못하지, 애초에 self 값도 없음.
# Student.detail_intfo()
Student.detail_info(studt1) #이렇게 self가 될 애를 넣어주면 가능하지.
Student.detail_info(studt2)
print()
print()


# 비교
# 해당 인스턴스의 class를 알려줌.
# 인스턴스만 보고 얘가 뭔지 모를수가 있잖아.
print(studt1.__class__, studt2.__class__)
print(id(studt1.__class__) ==  id(studt2.__class__)) #True
print()

# Instance Variables
# 직접 접근(PEP 문법으로 권장하지 않음)
studt1._name = 'JUST KIDDING'
studt1.___name = 'JUST KIDDING2'
#이렇게 하는것을 권장하지 않음. 무결하지가 않음.
#내가 지정한 메소드 등을 통해서 수정할 수 있게 해야함.
#Private, static, 등 접근 제어자에 대해서 추후에 나옴.
print(studt1.__dict__)
print(studt1._name, studt2._name)
print(studt1._email, studt2._email)

print()
print()
#클래스 변수는 누구나 접근 가능.
print(studt1.student_count)
print(studt2.student_count)
print(Student.student_count)
print()
print()

#Class Dictionary Name Space에는 무엇이 있을까?
#공유 확인
print(Student.__dict__)
print(studt1.__dict__) #여기에는 student_count라는 변수가 없음.
print(studt2.__dict__) #여기에는 student_count라는 변수가 없음.

# 인스턴스 네임스페이스에 없으면, 파이썬이 알아서 상위에서 검색함.
# 즉, 동일한 이름으로 변수 생성 가능(파이썬이 알아서 인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스) 검색함)
# 당연히 역은 성립하지 않음. 클래스 변수로 찾기 시작했는데, 인스턴스 와서 찾아보는것은 아님.
#print(Student._name) 이런거 안된다는 것.

#사실 del이런거는 오버라이딩 잘 안함.
#다른 방식들이 많이 있음. 이런 파이썬이 내부적으로 알아서 움직이는 것 들은 잘 안건듬.
del studt2
print(studt1.student_count)
print(Student.student_count)



