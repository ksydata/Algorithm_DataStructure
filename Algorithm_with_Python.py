#!/usr/bin/env python
# coding: utf-8

# In[1]:


### 모두의 알고리즘 with Python ###
## 제1장. 알고리즘 기초 ##


# In[6]:


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


# In[8]:


# 1. 절댓값 구하기 알고리즘 (2) 제곱 후 제곱근

def abs_square(a):
    b = a**2 
        # [제곱 a*a]
    return math.sqrt(b)
        # [수학모듈의 제곱근 함수]
abs_square(-4)


# In[62]:


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


# In[60]:


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


# In[61]:





# In[69]:


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


# In[84]:


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


# In[85]:


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


# In[ ]:





# In[ ]:


# 3. 주어진 숫자 n개 중 최댓값 찾기 알고리즘
# [list function] len()_append()_insert(i, x)_pop(i)_clear()_x in a

# [SY version]

def max_search(n):
    list = [17, 92, 18, 58, 7, 33, 42]
    
    for i in list:
        if len(list) % 2 != 0:
            list[len(list) / 2]

