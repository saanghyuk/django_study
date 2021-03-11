#Section07-1
#파이썬 클래스 상세 이해
#Self, Class, Instance Variable

#선언
#class name:
#   function
#   function
#   function

#Class는 첫 글자 대문자로, 단어와 단어가 연결된 경우 CamelCase
#Name space -> instance가 가지고 있는 공간
class UserInfo:
  #property, method
  def __init__(self, name):
    self.name = name
    print("클래스 초기화: ", name)
  def user_info_p(self, dish):
    print('Name : ', self.name)
    print('Favorite Food : ', dish)

user1=UserInfo("손상혁")

user1.user_info_p("쿠키")
user2 = UserInfo("Park")
user2.user_info_p("Pizza")
print("__dict__")
#Class 변수 check
print(user1.__dict__)
print(user2.__dict__)

#Class와 Instance의 차이 중요함.
#네임스페이스는 객체를 인스턴스화 할 때 저장공간을 의미함.
#클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
#인스턴스 변수는 객체 마다 별도로 존재.


#예제 2. 셀프의 이해
class SelfTest:
  def function1(): #self를 안넣으면 Class Method라는 선언
    print("function1 called")
  def function2(self): #self를 넣으면 Instance Methods, self인자를 받는데, Self가 없으면 어케받어.
    print(id(self))
    print("function2 called")


self_test = SelfTest()
# self_test.function1() #function1은 SELF를 안넣으니깐 error가 터짐.
#function1은 Self가 없어서 누구의 함수 인지를 모르는 거야.
# self가 들어있어야 현재 객체의 함수라는 것을 알려주는 건데, 셀프가 없으면 몰라
#근데 몰라도 뭐 클래스로 직접 접근하면 호출은 되지
SelfTest.function1()
print("selfTest.functiono1()")
# self_test.function1()
# 반대로 인스턴스 객체는 클래스 함수 호출을 못하나봐
# SelfTest.function2() #이건 Instance Method라서 여기서 호출이 안됨.


print(id(self_test))
self_test.function2() #같음
print(id(SelfTest))


#에제 3
#클래스 변수, 인스턴스 변수
class WareHouse:
  stock_num = 0
  def __init__(self, name):
    self.name = name
    WareHouse.stock_num+=1 #Class변수는 Class변수대로 카운팅 되고 있네
  def __del__(self): #인스턴스 종료될때 호출되는 Method
    WareHouse.stock_num-=1

user1 = WareHouse('Kim')
user2 = WareHouse('Son')
user3 = WareHouse('Yoon')

#Instance Name Space
print(user1.__dict__) #Self의 변수들이 나옴.
print(user2.__dict__)
print(user3.__dict__)

#Class Name Space
print(WareHouse.__dict__) #Class 변수들은 이렇게 찍으면 이렇게 나옴, Class변수는 공유,

print(user1.name)
print(user2.name)
print(user3.name)

#class 변수 접근 가능. 자기의 네임스페이스에 없으면, Class 네임스페이스로 가서 찾음.
#근데 class method에는 접근을 못하더라.
print(user1.stock_num)




#
del user1 # class 삭제 가능