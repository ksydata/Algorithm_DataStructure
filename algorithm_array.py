#!/usr/bin/env python
# coding: utf-8

## 파이썬을 이용한 알고리즘의 이해 ##
# 제7장. 배열 Array

# 7.3.(1) 세 수의 합
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [브루스 포스로 풀이] 무차별 대입 방식
        # [합이 "0"인 3수 리턴]
        
        # [SY first version]
        nums = nums.sort() 
                # [일단 정렬]

        for n in nums:
            n += 1
            if nums[n:n+2].sum() == 0:
                return nums[n] nums[n+1] nums[n+2]
            else: 
                # [Error] Invalid Syntax
                

