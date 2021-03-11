#Section07-2
#파이썬 클래스 상세 이해
#상속, 다중상속

#예제 1
#상속 기본
#슈퍼클래스(부모) 및 서브클래스(자식)
#자식은 다 물려받았기 때문에, 모든 속성 및 메소드를 사용 가능함.

#라면 -> 속성(종류, 회사, 맛, 면 종류, 이름 등): 부모
#자식 -> 공통을 사용하고 +알파를 추가하는 거지.

class Car:
  """Parent Class""" #보통 이렇게 해주는게 국룰
  def __init__(self, type, color):
    self.type = type
    self.color = color

  def show(self):
    return "This Car's sClass \'Show Method!\' "

class BmwCar(Car):
  """Sub Class"""
  def __init__(self, car_name, type, color):
      super().__init__(type, color) #부모한테 넘겨주기
      self.car_name = car_name
      print("Your Car Name: %s" % self.car_name)
  def show_model(self):
      return "Your Car Name: %s" % self.car_name

#자식 class 내부에서 부모 CALl할때는 super().function()으로 호출하면 됨.
class BenzCar(Car):
  """Sub Class"""
  def __init__(self, car_name, type, color):
      super().__init__(type, color) #부모한테 넘겨주기
      self.car_name = car_name
  def show_model(self):
      return "Your Car Name: %s" % self.car_name
  def show(self): #Overriding, 부모한테 있는 메소드를 써놓으면 덮어쓰기가 되는 것.
      print(self.type)
      print(super().show()) #부모에 있던거 한번 호출 하고.
      return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color)

#일반 사용
model1 = BmwCar('520d', 'sedan', 'red')
print(model1.color) #from super
print(model1.type) #from super
print(model1.car_name) #from sub
print(model1.show()) #from super
print(model1.show_model()) #from sub
print(model1.__dict__) #부모에서 상속받은 property 까지 다 나옴

#Method Overriding
model2 = BenzCar('220d', 'suv', 'Black')
print(model2.show())


#Parent Method Call
model3 = BenzCar("350s", 'sedan', 'silver')
print(model3.show())



#Inheritance
print(BmwCar.mro()) #왼쪽에서 오른쪽 방향으로 보면 되.
print(BenzCar.mro()) #왼쪽에서 오른쪽 방향으로 보면 되.

#예제2
#다중 상속
class X(object): #모든 클래스는 object class를 상속
  pass

class Y():
  pass

class Z():
  pass

class A(X, Y): #A는 X와 Y 상속
  pass

class B(Y, Z): #B는 Y와 Z 상속
  pass

class M(B, A, Z): #B는 Y와 Z 상속
  pass

print(M.mro())

#상속은 언제나 앞에 있는 것부터 영향을 받음.

