#!/usr/bin/env python
# coding: utf-8

## 머신러닝(회귀분석 모듈 구현)을 위한 파이썬 ##

## 제1장.제1절. Pythonic Code ##
# 1.1. Split & Join

items = "zero one two three".split() 
    # 빈칸을 기준으로 문자열 나누기
    # 활용 : News data, Bag of words
print(items)


example = "python, jquery, javascript"
example.split(",")
    # ","을 기준으로 문자열 나누기
a, b, c = example.split(",")
    # list에 있는 각 값을 a, b, c 변수로 unpacking
print(c)


example = "cs50.gachon.edu"
    # "."을 기준으로 문자열 나누고 unpacking
a, b, c = example.split(".")
print(a)


colors = ["red", "blue", "green", "yellow"]
result = "".join(colors)
result


# 1.2. List Comprehension and Nested For loop

result = []
for i in range(10):
    result.append(i)
result

result = [i for i in range(10)]
result # list comprehension

result = [i for i in range(10) if i % 2 == 0]
result # filter를 건 list comprehension


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

    
# 1.4. Lambda : 함수 이름 없이, 함수처럼 쓸 수 있는 익명함수
    # 수학의 람다 대수에서 유래, Python3부터 권장하지 않지만 여전히 쓰임

f = lambda n, k : n ** k
print( f(2, 30))
    # 시간복잡도 n의 k제곱

import numpy as np

f = lambda n, k : n * k
print( f(100, np.log(20)) )
    # 시간복잡도 n * logk
    

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


# Reduce function : legacy libraray에서 머신러닝 코드에서 여전히 사용

from functools import reduce

print( reduce(
    lambda x, y: x*y, 
    [1, 8, 1, 5, 1, 1, 8]
) )
    # (((((1*8)*1)*5)*1)*1)*8


def factorial(n):
    return reduce(
        lambda x, y: x*y,
        range(1, n+1)
    )
factorial(5)
    # 5*4*3*2*1


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


def asterisk_test(a, *args):
    print(a, args[0])
    print(type(args))
asterisk_test(1, (2,3,4,5,6))

def asterisk_test(a, *args):
    print(a, args)
    print(type(args))
asterisk_test(1, (2,3,4,5,6))
    # 튜플 타입으로 

    
data = ([1,2], [3,4], [5,6])
print(*data)
    # asterisk - upacking a container
    
def asterisk_test(a, b, c, d,):
    # tuple type (,)
    print(a, b, c, d)
data = {"b" : 1, "c" : 2, "d":3}
asterisk_test(4, **data)


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


deque_list.rotate(2)
print(deque_list)
deque_list.rotate(2)
print(deque_list)

deque_list.extendleft( [5,6,7] )
    # .expend는 right
print(deque_list)

print(deque( reversed(deque_list) ))


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

    
import time

start_time = time.clock()
    # AttributeError: module 'time' has no attribute 'clock'

dequeList = deque()
    # Stack
for i in range(2**7):
    dequeList.append(i)
    dequeList.pop()
print(time.clock() - start_time, "seconds")


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

    
d = OrderedDict()
d["SK"] = 100
d["KB"] = 300
d["LG"] = 200
d["HD"] = 500

for k, v in OrderedDict(sorted(d.items(), 
                               key = lambda t: t[0])).items():
    print(k, v)

    
for k, v in OrderedDict(sorted(d.items().
                              reverse = TRUE, key = ))


## 제4장. 로지스틱 회귀분석모형 구현 ##

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
    # [Error]
    # import tensorflow as tf
    # tf.compat.v1.disable_eager_execution()

data_train = pd.read_csv(
    "C:\PDSR\RforStatistics_FinalProject/data_train_py.csv", 
    index_col = 0)
    # [R로 데이터 전처리 완료한 csv.file read]
'''
    file = open(
        "C:\PDSR\RforStatistics_FinalProject/data_train_py.csv",
        "r", encoding = "UTF-8")
    reader = csv.reader( file )
    for line in reader:
        print( line )
    file.close()
    
    writer = csv.writer( file )
    writer.writerow( [list] )
    file.close()
'''

type(data_train)
np.random.seed(12345)
    # [set a seed for reproducible results]
    # [binary classification uses sigmoid function]
from sklearn.base import BaseEstimator, ClassifierMixin


class BinaryLogisticReg( BaseEstimator, ClassifierMixin ):
    # [클래스를 이용하여 교차 유효성 검사를 추가로 수행할 수 있도록]
    # [BaseEstimator와 ClassifierMixin class를 상속 결정] sklearn cross_val_score
    
    # 1. 매개변수를 무작위로 초기화
    def __init__(self):
        self.params = {}
        self.verbose = 0
        
    def init_params(self, X):
        n_features = X.shape[1]
            # [number of features]
        self.params["coef"] = np.random.randn(n_features, 1)
            # [the matrix for slope coefficients]
        self.params["intercept"] = np.random.randn(1, 1)
            # [the y-intercept]
        
        if self.verbose:
            print("[INFO] Initialized parameters")
            print(f"Shape of coefficinet matrix : {self.params["coef"].shape}")
            print(f"Shape of intercept matrix : {self.params["intercept"].shape}")

    # 2. 현재상태의 모델로 확률을 얻기 위해 예측 수행
    def get_logits(self, X, y = None):
        if "coef" not in self.params:
            # [initialize parameters if haven't]
            self.init_params(X)
        return X @ self.params["coef"] + self.params["intercept"]
            # [logits = log(odds) = X@W + b]
    
    def predict_proba(self, X, y = None):
        logits = self.get_logits(X)
        return 1 / 1 + np.exp(-logits)
            # [Sigmoid function]
            # [Used to get probability for binary class]
    
    def fit(self, X, y, learning_rate = 0.05, iterations = 1000, verbose = 0):
        self.verbose = verbose
            # [set verbose to 1 to see the entire training progress]
        
        if isinstance(X, pd.Dataframe):
            X = X.values
            self.init_params(X)
                # [initialize parameters]
            m = X.shape[0]
                # [number of samples]
        
        if verbose:
            print("[INFO] Traing ... ")
        
        # 3. 비용함수에 대한 미분 계산 & 경사하강법을 사용하여 매개변수 업데이트
        for i in range(1, iterations + 1):
            y_proba = self.predict_proba(X)
            # [make predictions by computing probability]

            loss = - (1/m) * np.sum(y * np.log( y_proba )\
                                   + (1 - y) * np.log( 1 - y_proba ))
            # [calculate the binary cross-entropy loss]
            
            dw = (1/m) * (X.T @ (y_proba - y))
            db = (1/m) * np.sum(y_proba - y)
            # [calculate gradients via deribatives]
            # [with respect to loss function (refer above)]
            
            self.params["coef"] -= (learing_rate * dw)
            self.params["intercept"] -= (learning_rate * db)
            
            if verbose and (i == 1 or i % 100 == 0):
                print(f"\nIteration {i} / {iterations}")
                print("--" * 12)
                print(f"Loss : {loss}")
                print(f"Coefficient : \n{self.params["coef"]}")
                print(f"Intercept : \n{self.params["intercept"]}")
    
    def predict(self, X, threshold = 0.5):
        y_proba = self.predict_proba(X)
        y_pred = np.where(y_proba > threshold, 1, 0)
        return y_pred
    
    def predict_score(self, X, y):
        from sklearn.metrics import accuracy_score
        y_pred = self.predict(X)
        return accuracy_score(y, y_pred)
        
        
