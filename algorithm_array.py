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
    
   
# 7.1.(1) 두 수의 합

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스 리턴]
        # [조건: 두 수의 합 = 9]

        nums = nums.sort()
        i, j = 0, 0
        if i in range(0, len(nums) - 1):
            if j in range(1, len(nums) - 1):
                # [시간복잡도 i, j O(n**2)]    
                # [코드 에러] range() 문법, i & j 초기화, j의 range()
                
                if nums[i] + nums[j] == target:
                    return [i, j]


