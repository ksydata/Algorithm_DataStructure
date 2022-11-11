#!/usr/bin/env python
# coding: utf-8


### 파이썬을 이용한 알고리즘의 이해 ###

## 제1장 1차원, 2차원에서 극댓값 찾기 ##
## 제2장 계산 모델 ##


# 문서 거리 알고리즘 #
# (1) split document to word (2) count word frequency (3) calculate scalar product of vectors(벡터의 내적, 각도)


# (1) 문서 내 단어의 빈도 연산 시 정규표현식 이용하는 구조화된 유사 코드(pseudo code)
# re.findall(r "\wt", doc)

char = 0
doc = 0
for char in doc:
    
    doc = ["digitaldevice", "retail", "financialcredit", "mobility"]
    
    if not alphanumeric:
        add previous word
    if any to list: 
        start new word
            # 조건문에서 O(1) 상수의 시간 복잡도 
        # 총 문서 내 단어의 빈도 연산 O(2^n) 부분집합만큼 즉, 지수형 시간 복잡도


# (2) 단어 리스트 정렬 *word : 자연로그 이상의 비트인 객체가 레지스터 메모리에 들어있는 경우

word = 0
list = 0
for word in list:
    
    doc = ["digitaldevice", "retail", "financialcredit", "mobility"]
    
    if same as last word:
        increment counter
    else:
        add last word and count to list
        reset counter to 0
            # O(1)
        # O(k*logk*|word|)


# (3) Dictionary Approach

doc = []
count = {}
for word in doc:
    
    doc = ["digitaldevice", "retail", "financialcredit", "mobility"]
    
    if word in count:
        count[word] += 1
            # O(1) key에 해당하는 value의 frequency를 counting
    else: count[word] = 1


### 모두의 알고리즘 with Python ###
## 제1장. 알고리즘 기초 ##


# 1. 절댓값 구하기 알고리즘 (1) 부호 판단

'''
[SY version]
def abs_sign(a):
    a = 0
    if a >= 0:
        a = a
    else a < 0:
        a = -a
'''

import math
    # [수학 모듈 사용]
    
def abs_sign(a):
    if a >= 0:
        return a
    else:
        return -a
    # [절댓값 알고리즘 1] 부호판단
    # [입력] 실수 a
    # [출력] a의 절댓값

abs_sign(-2)


# 1. 절댓값 구하기 알고리즘 (2) 제곱 후 제곱근

def abs_square(a):
    b = a**2 
        # [제곱 a*a]
    return math.sqrt(b)
        # [수학모듈의 제곱근 함수]
abs_square(-4)


# 2. 1부터 n까지 합 구하기 알고리즘
# (1) n = 10
# (2) n = 100

# [SY version 1]
def two_num_of_sum(n):
    for i in range(10):
        # n = 0
        # i = 0
            # [i = 0] : 20
            # [if not] : 65
        i += 1
        n += i
    return n

two_num_of_sum(10)

'''
[SY version 2]
f= lambda n : n*(n - 1)/2 if input(n) else return "error"
'''

# [SY version 3]
def two_num_of_sum(n):
    for i in range(10):
        i += 1
        n = i*(i + 1)/2
    return n
    
two_num_of_sum(10)


'''
[1부터 n까지 합 구하기 알고리즘]

i. "합을 기록할 변수 s"를 만들고 0을 저장
ii. 변수 i를 만들어 1부터 n까지의 숫자를 1씩 증가시키며 반복
iii.[반복 블록] 기존의 s에 i를 더하여 얻은 값을 다시 s에 저장
iv. 반복이 끝났을 때 s에 저장된 값 = 결과값
'''

def twonum_of_sum(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s

twonum_of_sum(10)


from dataclasses import dataclass
    # [파이썬 구조체와 클래스 구현]
    
@dataclass
class Rectangle:
    width : int
    height : int
    
    def area(self):
        return self.width * self.height
    
rect = Rectangle(3, 4)
rect.area()


# 2. 1부터 n까지 연속한 숫자의 제곱 합 구하기 알고리즘

# [SY version]

import timeit
 
start_time = timeit.default_timer() 
    # [시작 시간 체크]
 
def num_squared_sum(n):
    s = 0
    for i in range(1, n+1):
        s = s + i**2
    return s

num_squared_sum(10000)

terminate_time = timeit.default_timer() 
    # [종료 시간 체크]
    
print("%f초 걸렸습니다." % (terminate_time - start_time)) 
    # [0.008897초]


import timeit
 
start_time = timeit.default_timer() 
    # [시작 시간 체크]
 
def num_squared_sum(n):
   return n * (n + 1) * (2*n + 1) // 6

num_squared_sum(10000)

terminate_time = timeit.default_timer() 
    # [종료 시간 체크]
    
print("%f초 걸렸습니다." % (terminate_time - start_time)) 
    # [0.000257초]


# 3. 주어진 숫자 n개 중 최댓값 찾기 알고리즘
# [list function] len()_append()_insert(i, x)_pop(i)_clear()_x in a

# [SY version]

def max_search(n):
    list = [17, 92, 18, 58, 7, 33, 42]
    
    for i in list:
        if len(list) % 2 != 0:
            list[len(list) / 2]

            
# [자료형 시간복잡도]
            
a = [1, 8, 1, 5, 1, 1, 8]

# O(1)
len(a)
a[0]
# a[key] 키를 조회하여 값을 리턴
# a[key] = value 키 값을 삽입
# key in a
a[5:8]
a.append(elem)
a.pop() 
    # [stack] deque
a.pop(0)

# O(n)
elem in a
a.count(elem)
a.index(elem)
del a[1]
a.reverse()
min(a)
max(a)

# O(nlogn)
a.sort()
    # [Timsort]     
    
  
# 제6장. 문자열 조작

# 6.1. 유효한 팰린드롬 여부 판별하는 알고리즘
# 6.1.(1) 리스트로 변환

def isPalindrome(self, s: str) -> bool:
    
    strs = "A man, a plan, a canal: panama"
    strs = strs.lower()
    strs = strs.split()

    strs = list(str(strs))
    print(strs)
        
    for char in s:
        if char.isalnum():
            # [숫자, 영문자 여부 판별하는 함수]
            strs.append( char.lower() )
    
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                # 팰린드롬 여부를 판별하는 함수
                return False
    return True

        
# 6.1.(3) 슬라이싱

def isPalindrom(self, s: str) -> bool:
    s = s.lower()
    s = re.sub( "[^a-z0-9]", "", s )
        # [영숫자만 걸러내도록 정규식으로 불필요한 문자 필터링]
    return s == s[::-1]
        # [문자열 슬라이싱 및 역순으로 뒤집기 s.reverse]
    
    
# 6.1.(2) 데크 자료형을 이용한 최적화

def isPalindrom(self, s: str) -> bool:
    
    strs = ["a", "m", "a", "n", "a", "p", "l", "a", "n", "a", "c", "a", "n", "a", "l", "p", "a", "n", "a", "m", "a"]
    strs: Deque = collections.deque()
         # [자료형을 데큐로 선언]
    
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                # [strs.pop()은 시간복잡도 O(n)이지만, strs.popleft()는 O(1)]
                return False
            
        return True

s.isPalindrom()
    # [AttributeError: 'list' object has no attribute 'isPalindrom']

    # [딕셔너리와 관련된 컨테이너 자료형]
        # collections.defaultdict()
        # collections.Counter()
        # collections.Ordereddicted
        
        
# 6.2. 문자열 뒤집는 알고리즘 : 리턴 없이 리스트 내부를 직접 조작하라는 제약 사항 有

# 6.2.(1) 투 포인터를 이용한 리스트 내부 스왑 방식

s = ["a", "w", "a", "y"]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0 
        right = len(s) - 1

        while left <= right: 
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
    # [We will use two pointers, one from start and one from end]
    # [We will swap the chars and increment the left and decrement the right]

    
# 6.2.(2) 파이써닉 코드

class Solution:
    def reverseString(self, s: list[str]) -> None:
        s = s[::-1]
        s.reverse()


# 6.3. 로그 파일 재정렬하는 알고리즘        
        
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
            # [0. 요구조건을 깔끔하게 처리할 것]
            # [1. 람다 + 연산자 이용한 로그를 재정렬함 (logs)]
            # [2. 문자로 구성된 로그가 숫자 로그보다 우선함 (letters > digits)]
            # [3. 식별자는 순서에 영향을 미치지 않지만 문자가 동일할 경우 식별자 순으로 함]
            # [4. 숫자로그는 입력 순서대로 함]

        if logs == logs.split()[1].isdigit:
            digits.append(logs)
        else:
            letters.append(logs)
        
        letters.sort( key = lambda x: (x.split()[1:], x.split()[0]) )
            # [2개의 key를 람다 표현식으로 정리]
        return letters + digits

