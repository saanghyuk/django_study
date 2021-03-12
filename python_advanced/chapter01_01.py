
#Chapter01-1
#파이썬 심화
#객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
#클래스 상세 설명
#클래스 변수와 인스턴스 변수

#절차지향은 왼쪽에서 오른쪽으로 위에서 아래로 내려오면서 실행이 됨.
#컴퓨터의 처리구조와 유사해서 실행속도가 빠름.
#그런데 위 아래로 몇천줄? 유지보수가 어려움. 이해가 어려움
#위, 아래 순서가 뒤바뀌면 예외가 발생함.

#일반적인 코딩
#학생 1
student_name_1 = 'KIM'
student_number_1 = 1
student_grade_1 = 1
student_detail_1 = [
  {'gender': 'Male'},
  {'score1': 95},
  {'score2':88}
]
#학생 2
student_name_2 = 'SON'
student_number_2 = 2
student_grade_2 = 2
student_detail_2 = [
  {'gender': 'Female'},
  {'score1': 77},
  {'score2':92}
]
#학생 3
student_name_3 = 'YOON'
student_number_3 = 3
student_grade_3 = 3
student_detail_3 = [
  {'gender': 'Male'},
  {'score1': 99},
  {'score2': 100}
]

#리스트 구조
student_names_list=['KIM', 'SON', 'YOON']
student_numbers_list=[1, 2, 3]
student_grades_list =[1, 2, 4]
student_details_list=[
  {'gender': 'Male', 'score1': 95, 'score2':88},
  {'gender': 'Female', 'score1': 77, 'score2':92},
  {'gender': 'Male', 'score1': 99, 'score2': 100},
]

#학생 삭제
del student_names_list[1]
del student_numbers_list[1]
del student_grades_list[1]
del student_details_list[1]

print(student_names_list)
print(student_numbers_list)
print(student_grades_list)
print(student_details_list)
#리스트 구조
#관리하기 불편
#데이터의 정확한 위치(인덱스)를 매핑해서 사용해야 함.


print()
print()


#딕셔너리 구조
#코드 반복 지속, 중첩문제
students_dicts = [
  {'student_name':'KIM', 'student_number':1, 'student_grade':1,
  'student_dtail': {'gender':'Male', 'score1':95, 'score2':88 }},
  {'student_name':'SON', 'student_number':2, 'student_grade':3,
  'student_dtail': {'gender':'Femail', 'score1':77, 'score2':92 }},
  {'student_name':'YOON', 'student_number':3, 'student_grade':4,
  'student_dtail': {'gender':'Mail', 'score1':99, 'score2':100 }}
]

del students_dicts[1]
print(students_dicts)

print()
print()

