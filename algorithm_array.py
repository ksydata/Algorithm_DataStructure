#!/usr/bin/env python
# coding: utf-8

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [브루스 포스로 풀이]
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
                

