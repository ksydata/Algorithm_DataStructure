#!/usr/bin/env python
# coding: utf-8

# In[1]:


## 머신러닝(회귀분석 모듈 구현)을 위한 파이썬 ##


# In[2]:


## 제1장.제1절. Pythonic Code ##
# 1.1. Split & Join

items = "zero one two three".split() 
    # 빈칸을 기준으로 문자열 나누기
    # 활용 : News data, Bag of words
print(items)


# In[3]:


example = "python, jquery, javascript"
example.split(",")
    # ","을 기준으로 문자열 나누기
a, b, c = example.split(",")
    # list에 있는 각 값을 a, b, c 변수로 unpacking
print(c)


# In[4]:


example = "cs50.gachon.edu"
    # "."을 기준으로 문자열 나누고 unpacking
a, b, c = example.split(".")
print(a)


# In[5]:


colors = ["red", "blue", "green", "yellow"]
result = "".join(colors)
result


# In[ ]:





# In[6]:


# 1.2. List Comprehension and Nested For loop

result = []
for i in range(10):
    result.append(i)
result

result = [i for i in range(10)]
result # list comprehension

result = [i for i in range(10) if i % 2 == 0]
result # filter를 건 list comprehension


# In[7]:


word_1 = "New"
word_2 = "Impact"
result = [i+j for i in word_1 for j in word_2]
    # for i in word_1:
        # for j in word_2:
    # Nested For Loop
print(result, ",")

result2 = [i+j for i in word_1 for j in word_2 if not (i == j)]
print(result2, ",")

result3 = [ 
    [i+j for i in word_1] for j in word_2
        # 바깥쪽 for문이 먼저 고정
]
print(result3)


# In[8]:


words = "The quick brown box jumps over the lazy dog".split()
    # 2차원 list comprehension
    # 문장을 빈칸 기준으로 분리하여 list로 변환
stuff = [
    [w.upper(), w.lower(), len(w)] 
    # 대문자, 소문자, 길이
     for w in words
]
for i in stuff:
    print(i)


# In[ ]:





# In[9]:


# 1.3. Enumerate : list의 element를 추출할 때 번호를 붙여서 추출
# Zip : 두 개의 list의 값을 병렬적으로 추출

for i, v in enumerate( ["tic", "tac", "toe"] ):
    print(i, v)
    # list에 있는 index와 값을 unpacking
    
mylist = ["a", "b", "c", "d"]
list(enumerate( mylist ))
    # list에 있는 index와 값을 unpacking하여 list로 저장

{i:j for i,j in enumerate(
    "Sookmyung Women's University is an academic institute located in South Korea".split() 
)}
    # 문장을 list로 만들고 list의 index와 값을 unpacking하여 dictionary type으로 저장


# In[10]:


result1 = ["N", "L", "H"] # level
result2 = ["none", "low risk", "high risk"] # meaning
for l, m in zip(result1, result2):
    print(l, m)
    
for i, (l, m) in enumerate( zip(result1, result2) ):
    print("\n")
    print(i, l, m)


# In[11]:


# ValueError : not enough values to unpack
# i, M = zip( (1,2,3), (0, 100, 500) )
    # 각 tuple의 같은 index끼리 묶음 
    # 계산 모듈
[sum(x) for x in zip( (1,2,3), (0, 100, 500) )]
    # 각 tuple, 같은 index를 묶어 합을 list로 변환


# In[ ]:





# In[12]:


# 1.4. Lambda : 함수 이름 없이, 함수처럼 쓸 수 있는 익명함수
    # 수학의 람다 대수에서 유래, Python3부터 권장하지 않지만 여전히 쓰임

f = lambda n, k : n ** k
print( f(2, 30))
    # 시간복잡도 n의 k제곱

import numpy as np

f = lambda n, k : n * k
print( f(100, np.log(20)) )
    # 시간복잡도 n * logk


# In[13]:


# Map function : sequence 자료형의 각 element에 동일한 function을 적용함
    # map reduce 개념 추후 학습
    
ex = [1, 8, 1, 5]
f = lambda x: x ** 2
print( list(map(f, ex)) )
print( map(f, ex) ) 
    # 주소값만 출력

# ver1. lambda
list( map(
    lambda x: x ** 2 if x % 2 == 0 else x, ex
)) 
    # lambda function은 반드시 else값을 넣어주어야 함

# ver 2. list comprehension
[v ** 2 
 for v in ex]
    # function
    # value in list


# In[14]:


# Reduce function : legacy libraray에서 머신러닝 코드에서 여전히 사용

from functools import reduce

print( reduce(
    lambda x, y: x*y, 
    [1, 8, 1, 5, 1, 1, 8]
) )
    # (((((1*8)*1)*5)*1)*1)*8


# In[15]:


def factorial(n):
    return reduce(
        lambda x, y: x*y,
        range(1, n+1)
    )
factorial(5)
    # 5*4*3*2*1


# In[ ]:





# In[16]:


# 1.5. Asterisk : 흔히 아는 *, 단순제곱-제곱연산-가변인자 활용 등 다양하게 사용
    # open source code에 많음
    # * unpacking, 풀어서 던져줌
    
# 예제 코드 #
def asterisk_test(a, *args):
    # 가변 인자
    print(a, args)
    print(type(args))
asterisk_test(1,2,3,4,5,6)
asterisk_test(2,1,3,4,5,6)

def asterisk_test(a, args):
    print(a, *args)
    # * unpacking container : 중요
    print(type(args))
asterisk_test(1, (2, 3, 4, 5, 6))

def asterisk_test2(b, **kargs):
    # 키워드 인자
    print(b, kargs)
    print(type(kargs))
asterisk_test2(1, c = 2, d = 3, e = 4, f = 5, g = 6)
    # dictionary type


# In[17]:


def asterisk_test(a, *args):
    print(a, args[0])
    print(type(args))
asterisk_test(1, (2,3,4,5,6))

def asterisk_test(a, *args):
    print(a, args)
    print(type(args))
asterisk_test(1, (2,3,4,5,6))
    # 튜플 타입으로 


# In[18]:


data = ([1,2], [3,4], [5,6])
print(*data)
    # asterisk - upacking a container
    
def asterisk_test(a, b, c, d,):
    # tuple type (,)
    print(a, b, c, d)
data = {"b" : 1, "c" : 2, "d":3}
asterisk_test(4, **data)


# In[ ]:





# In[19]:


# 1.5. tuple, dict에 대한 확장 데이터 구조 : Collections 내 모듈
    # deque(Queue, Stack) : rotate, reverse 등 linked list 특성 지원
    # counter, orderedDict, defaultdict, nameedtuple

# 큐, 스택

from collections import deque

deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(deque_list)

deque_list.appendleft(10)
print(deque_list)


# In[21]:


deque_list.rotate(2)
print(deque_list)
deque_list.rotate(2)
print(deque_list)

deque_list.extendleft( [5,6,7] )
    # .expend는 right
print(deque_list)

print(deque( reversed(deque_list) ))


# In[27]:


from time import time
from collections import deque

def check():
    start = time()
    
    dequeList = deque()
    for i in range(2**7):
        dequeList.append(i)
        print(dequeList)
    return time() - start

print(check())
    # 0.017951011657714844


# In[36]:


import time

start_time = time.clock()
    # AttributeError: module 'time' has no attribute 'clock'

dequeList = deque()
    # Stack
for i in range(2**7):
    dequeList.append(i)
    dequeList.pop()
print(time.clock() - start_time, "seconds")


# In[44]:


# Sorting {key : value}
    # OrderedDict
    
from collections import OrderedDict

d = {}
    # general dict
d["SK"] = 100
d["KB"] = 300
d["LG"] = 200
d["HD"] = 500

for k, v in d.items():
    print(k, v)


# In[45]:


d = OrderedDict()
d["SK"] = 100
d["KB"] = 300
d["LG"] = 200
d["HD"] = 500

for k, v in OrderedDict(sorted(d.items(), 
                               key = lambda t: t[0])).items():
    print(k, v)


# In[ ]:


for k, v in OrderedDict(sorted(d.items().
                              reverse = TRUE, key = ))

