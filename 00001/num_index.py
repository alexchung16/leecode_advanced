#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ File test.py
# @ Description 找到索引
# @ Author alexchung
# @ Time 7/9/2019 PM 14:39


# 方法一
def twoSum1(nums, target):
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    :param nums:
    :param target:
    :return:
    """
    for i in range(len(nums)):
        rest_nums = nums[:i]
        rest_num = target - nums[i]
        if rest_num in rest_nums:
            j = rest_nums.index(rest_num)
            return [j, i]
        else:
            continue


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result1 = twoSum1(nums, target)
    print(result1)
