# Chapter05-2
# 파이썬 심화
# 파이썬 클래스 특별 메소드 심화 활용 및 상속

# Class ABC(abstract class)

# class 선언
class VectorP_sample(object):
  def __init__(self, x, y):
    self.__x = float(x)
    self.__y = float(y)

  def __iter__(self):
    # 아래 쓴거는 generator야. next호출 하면 x, 그 다음 호출하면 y가 나오라는 뜻.
    # 리스트를 통으로 보낼꺼면 []로 하면 됨.
    return (i for i in (self.__x, self.__y))

# 객체 선언
v_sample = VectorP_sample(20, 40)
#  print('EX1-1', v.__x, v.__y ) 파이썬에서 밑줄 두개를 놓으면, 감춰버림. error터짐.



# _x라고 해놨어. 그리고 생성할때, y가 40보다 큰지 init에서 체크한다음에 self에 넣었어.
# 근데 init에서 다 체크해놨더니 직접 접근이 가능해서 v._y = 10 해버리면?
# init에서 짜놨던게 싹다 무용지물이잖아.
# 심지어 float으로 넣어놨더니, 그것조차도 10이라는 int로 바뀌어버림.
# 은닉에 완전히 동떨어진 것.
# 그래서 init에서 체크하고, self에 할당하는 것은 그렇게 좋지는 않아.

# 그래서 나온 개념이 Getter, Setter
# 밑줄 두개로 해놔도 사실 값을 바꾸는 방법은 많아.
# _ 두개 붙인 후에, Getter, Setter를 활용하면 됨.

class VectorP(object):
  def __init__(self, x, y):
    self.__x = x
    self.__y = y

  def __iter__(self):
    # 아래 쓴거는 generator야. next호출 하면 x, 그 다음 호출하면 y가 나오라는 뜻.
    # 리스트를 통으로 보낼꺼면 []로 하면 됨.
    return (i for i in (self.__x, self.__y))

  @property
  def x(self):
    print('Called Property X')
    return self.__x

  #getter를 먼저 만들어야 함
  @x.setter
  def x(self, v):
    print('Called Property X Setter')
    self.__x = float(v)

  @property
  def y(self):
    print('Called Property Y')
    return self.__y

  #getter를 먼저 만들어야 함
  @x.setter
  def y(self, v):
    print('Called Property Y Setter')
    if v<30 :
      raise ValueError('30 Below is not possible')
    self.__y = float(v)


# Getter, Setter

v = VectorP(20, 40)
# print(v.__x) # 접근 불가
print(v.x) # 접근 가능해짐. 우리는 __로 정의했는데, 접근 가능해짐
v.x = 10
print(v.x)

print(v.y)
# v.y = 20 Error
v.y = 40
print(v.y)

print('EX1-2 -', dir(v), v.__dict__) # ['_VectorP__x', '_VectorP__y', 'x', 'y'] 알아서 이렇게 만들어져 있음.
# dict찍어보면 실제로 변수는 이렇게 저장되어 있는 것을 알 수 있음. 다만, 파이썬에서 자동으로 x로 호출 가능하게 해준거지.
print(v._VectorP__x)
print(v._VectorP__y)
print('EX1-3 - ', v.x, v.y)
# Iter확인. 그대로 돌리면 Generator에서 하나씩 풀리겠지.
for val in v_sample:
  print('EX1-4', val)



