
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')





# 파이썬 기초

# 주피터 노트북에서만 적용되는 버전확인
# !python -V


#표현식
print(273)
print(10 + 20 + 30)
"python programming"

# 표현식이 하나 이상 모이면 문장이 된다
print(52,'Hello Python', 5+3)


#문장이 모여서 프로그램이 된다
a=1;b=2;c=a+b;    #줄바꿈대신 ;사용 가능. ; 단위로 끊어준다는 의미
print(c)
print()

# 키워드 알아보기
import keyword

print(keyword.kwlist)

print()

# 식별자 기본 규칙
# 키워드 사용 불가
# 특수문자는 언더바(_) 만 사용 가능
# 숫자로 시작 불가
# 공백을 포함할 수 없다

# 가능 alpha
# 가능 _alpha
# 키워드라 사용 불가 break
# 숫자로 시작해서 불가   273alpha
# 공백 불가  has alpha


# 파이썬은 snake_case와 CamelCase를 모두 사용
# - itemlist item_list #snake_case 사용
# - ItemList # CamelCamse 사용 (앞글자만 대문자, 클래스 이름 쓸 때 사용함)
# - login_status #snake_case
# - LoginStatus #CamelCase
# - snake case(소문자로 시작), 뒤에 ()가 있으면 "함수"임
# - snake case(소문자로 시작), 뒤에 ()가 없으면 "변수"임


# 사람이 생각하는 방식을 그대로 표현할 수 있는 파이썬
if 3 in [1,2,3,4]:
    print('3이 있습니다')


if 'a' in ['a', 'p', 'p','l','e']:
    print('a in a')


if 'sea' in ['jay', 'koo', 'till', 'jam']:
    print('sea in a')
else:
    print('see not a')

print()


# 파이썬 자료형 - 숫자형 (정수, 실수, 8진수, 16진수)
a = 123
b = -123
c = 0
d = 1.23
type(d)
e = 0o177 #8진수 00 또는 00으로 시작
f = 0xABC #16진수 0x 로 시작
print(a,b,c,d,e,f)


print()

a = 10
b = 2
c= a + b
d = a * b
e = a / b #나누기
f = a % b #나눠서 나머지 구하기
g = a // b #나눠서 몫 구하기
h = 2 ** 3 # 제곱

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

print()


# string = "문자열"
# number = 273
# stirng + number >> 에러발생 문자열과 숫자형은 더하기 못함
# 붙여서 사용하려면 273을 '273'으로 해야 함

a = 10
a = "문자"
a = 100
print(type(a))

# 복합 대입 연산자

num = 10
num += 10  #위의 num 값에 10 더함
num *= 10 #위의 num 값에 10 곱함
print(num)


h = 50
h -= 10
h * 20
print(h)

# 사용자 입력 input
# input('인사말을 입력하세요')
#
# #input 활용
# num = input('숫자를 입력하세요 : ')
# print(num)
# type(num)
#
# # 문자 입력 후 붙여서 나오는 변수
# num1 = input('숫자를 입력하세요')
# num2 = input('숫자를 입력하세요')
# print(num1 + num2)
#
#
# ## 연산을 위한 형변환
# ##### input 함수를 사용하면 숫자도 문자로 전환, 숫자연산을 위해 int로 변환 필요
#
# num1 = input('숫자를 입력하세요')
# num1_n = int(num1)
# num2 = input('숫자를 입력하세요')
# num2_n = int(num2)
# print(num1_n + num2_n)
#
#
#
# # Q. 3과 3.3을 입력하고 숫자연산을 수행하여 6.3을 출력하세요
#
# num1 = input('숫자를 입력하세요')
# num1_n = int(num1)
# num2 = input('숫자를 입력하세요')
# num2_n = float(num2)
# print(num1_n + num2_n)
#
#
# # Q. 3과 3.3을 입력하고 숫자연산을 수행하여 6.3을 출력하세요
#
# num1 = input('입력 : num1')
# num1_n = int(num1)
# num2 = input('입력 : num2')
# num2_n = float(num2)
# print(num1_n + num2_n)


# Q. 3과 3.3을 입력하고 숫자연산을 수행하여 6.3을 출력하세요

a=3
b = 3.3
print(a+b)


# Q. a= 52, b=52.273 일 때 a+B는 5252.273으로 출력하도록 a와 b를 문자열 자료형으로 변환하세요
# a = input('숫자를 입력하세요 : ')
# b = input('숫자를 입력하세요 : ')
# print(str(num1_n) + str(num2_n))


a = '52'
b = '52.273'
print(a+b)

a = str(52)
b = str(52.273)
print(a+b)

# 문자열 표시방법

# 차이점
p1 = "python`s value is great"
p2 = 'python`s value is great' #어퍼스트로피 구분이 잘 안 되섬 비추
# p3 = 'python's value is great' ''가 중복으로 쓰여서 쓸 수 없음


s1 = '"python is valuable" he says'
print(s1)

# \ 사용 시 '를 텍스트로 인식
s2 = 'python\'s value is great'
print(s2)


# 여러 줄을 묶을 때 ''' '''를 사용
#\n 한 줄 띄기
y1 = "Once you study data analysis\nYou need pythin"
print(y1)
y2 = '''Once you study data analysis
You need pythin'''
print(y2)
y3 = """Once you study data analysis
You need pythin"""
print(y3)



# 문자열 연산
a1= 'Python'
a2 = ' is easy to learn'
print(a1 + a2)
print(a1 * 3)
print("="*20)


# 자료형 - List []
# 리스트는 [] 로 표시한다
# []안의 내용을 콤마로 구분하여 순서있게 나열한다

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d']
list3 = [1,'a','abc', [1,2,3,4,5],['a','b','c']] #숫자 문자 섞어서 사용 가능
print(list3)


# 인덱싱
list1 = [1,2,3,4,5]
list1[4]
list1[-1]
list1[0:5] #5에 해당하는 자료까지 잘라서 보여준다
list1[0:]
list3[2]
list3[3][4]
list3[4][1]


# 리스트 수정, 삭제
#import numpy as np
#a = np.arange(10).tolist()
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = ['a','b','c']
a[0] = 1 #기존 0번쩨에 있던 자료값을 1으로 수정
print(a)
b[1]='a'
print(b)

# 리스트에 있는 자료 삭제 del
del b[0] #b에 0번쩨에 있는 자료를 삭제
print(b)



# 가장 마지막에 있는 값을 바꾸기
c = a + b
c[-1] = 1
print(c)

# 맨 뒤에서 앞에 있는 값을 바꾸기
c[-2] = 2
print(c)


#  sort는 값 정렬
s = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 1]
s.sort()
print(s)

# 내림차순 reverse
s_d = sorted(s,reverse = True)
print(s_d)

s.reverse()
print(s)


#  index는 값이 몇번째에 있는지 알려준다
# c = np.random.randint(100, size=100).tolist()
# print(c)
# c.index(58)

# count는 개수 세줌
c = [1,1,3,3,3,5,5]
print(c.count(3))


# extend 리스트에 값 더 넣기 (2개 이상 추가)
h = [1,2,3]
h.extend([4,5])
print(h)
h.extend([6,7,'a','b','c'])
print('h - ',(h))

# append는 값 추가하기 (1개)
h.append(6)
print(h)
h.append(True)
print('h - ', (h))

# 튜플 ()
# 인덱싱 가능
# 튜플은 값을 변경할 수 없다

tuple1 = (1,2,3,4,5)
tuple2 = ('a','b','c')
tuple3 = (1,'a','abc',[1,2,3,4,5],['a','b','c'])


print(tuple1[0:2])
print(tuple1[1:5])
print(tuple1[0:3])
print(tuple1[3:6])
print(tuple2[0:4])
print(tuple2[0:])
print(list(tuple2[1:3]))
print(list(tuple1[1:5]))
print(tuple3[-1][2])
print(tuple3[-2][0])
print(list(tuple3[2]))
print(list(tuple3[-1][2]))



# 튜플은 이 특징 떄문에 그 값이 항상 변하지 않아야 하는 경우 사용한다

#리스트의 경우 값 변경 가능
list1[0] = 6
print(list1)

# 튜플의 경우 값 변경 불가
# tuple1[0] = 6
# print(tuple1)



# 튜플은 값이 1개만 있을 때는 값 뒤에 ,(콤마)를 붙여야 한다
t1 = (1,)
print(t1)
print()

# 콤마를 안 붙이면 튜플이 안 됨
t4 = 1
print(t4)
print(type(t4))

t2 = 1,2,3
print(t2)

#t2 타입 확인
print(type(t2))

# 튜플은 연산 가능
print(t2 *3)
t3 = t1 + t2
print(t3)


### 딕셔너리 자료형
### 특징 : 키와 값을 하나의 요소로 한다, 순서가 없다, 키로 값의 내용 바꿀 수 있음, 인덱싱이 없다 (키 값으로 값을 찾아야 한다)

d1 = {'a':1, 'b':2, 'c':3}
print(d1['a'])
d1['b']=5
print(d1)
print()

colors = {'a':'blue', 'b':'red','c':'orange','d':'purple','e':'white','f':'yellow'}
print(colors['b'])
print(colors)
print(colors.keys())
print(d1.keys())
print(colors.values())

#items
#튜플 형태로 인덱스, 밸류 모두 출력
print(colors.items())

print()

### 집합 (set)
### 중복 허용 x, 순서 없음, 인덱싱 불가
### 인덱싱 하려면 리스트나 튜플로 형변환 필요
s1 = set([1,2,5,4,3])
s2 = set('Hello')
print(type(s1), s1)
print(type(s2), s2)

s3 = set([1,2,3,4,5,6])
s4 = set([4,5,6,7,8,9])

print(list(s3|s4))
print(list(s3&s4))

print('-'*30)

# 들여쓰기

li = ['a','b','c']
if 'a' in li:
    print("'a' 가 li에 있습니다")
else:
    print("'a' li에 없습니다")


ko = 900
if ko > 1000:
    print('ko is small 1000')
else:
    print('ko is greater 1000')


money = False
if money:
    print("buy bike")
else:
    print("keep walking")


money = 10000
if money >= 50000:
    print("ride taxi")
else:
    print("fly to the sky")


money = 10000
card = True
if money >=30000 or card:
    print("ride taxi")
else:
    print("fly to the sky")


pocket = ['ticket', 'water', 'gum']
if 'money' in pocket:
    print("keep going hall")
else:
    print("back to the home")

print()

if 'money' in pocket:pass
else: print("back to the home")



#format 함수
f1 = "{} 선수가 {}등 입니다.".format('해밀턴', 1)
print(f1)

cat1 = "우리집에 {}번째로 온 고양이는 {}이다.".format(1,'까미')
print(cat1)


# 문자일 땐 s, 숫자일 땐 d
print("%s 선수가 %d등입니다." %("해밀턴", 1))
print("키 크기로는 %s가 %d등입니다"%("구미", 2))


#연습
# 파이썬은 자바보다 쉽습니다.
y1 = "%s은 %s보다 %d배 쉽습니다." % ("파이썬", "자바", 2)
print(y1)

#y2 = "{}는 {}보다 {}배 어렵습니다".format('자바', '파이썬' 2)

### format함수를 활용한 자릿수 확보 {:d}
### 정수는 d 앞에 원하는 자릿수 만큼 넣는다 (자릿수 확보)
### 소수는 f뒤에 원하는 자릿수 만큼 넣는다 (원하는 소수점까지 표시)
### 소수는 f앞에 원하는 자릿수 만큼 넣는다 (자릿수 확보)


ex2 = 12345
f2 = "{:d}".format(ex2)
print(f2)


f3 = '{:10d}'.format(ex2)
print(f3)

f4 = '{:f}'.format(ex2)
print(f4)


f5 = '{:10.2f}'.format(ex2)
print(f5)

### 제어문 : if~elif~else

### 수입과 지출 금액을 비굫서 수입이 많으면 저축증가, 반대이면 빚이 증가, 같으면 현상 유지

i = 500,000,000
e = 400,000,000

if i > e:
    print("저축증가")
elif i < e:
    print("빚이증가")
else:
    print("현상유지")



# for 반복문
numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    print(number)




#while은 조건이 만족되는한 무한 반복함
