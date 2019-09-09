#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ File num_index.py
# @ Description 求解列表中和为特定数值的元素索引
# @ Author alexchung
# @ Time 7/9/2019 PM 14:39

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
"""


def twoSum1(nums, target):
    """
     method 1
     使用 index 方法优化查找
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


def twoSum2(nums, target):
    """
     method 2
     字典模拟哈希
    :param nums:
    :param target:
    :return:
    """
    hashmap = {}
    # 建立哈希表
    for index, num in enumerate(nums):
        hashmap[num] = index
    for i in range(len(nums)):
        j = hashmap.get(target - nums[i])
        if j is not None and i != j:
            return [i, j]
        else:
            continue


def twoSum3(nums, target):
    """
     method 3
     优化哈希
    :param nums:
    :param target:
    :return:
    """
    hashmap = {}
    for i, num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i != j:
            return [j, i]
        else:
            hashmap[num] = i
            continue


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result1 = twoSum2(nums, target)
    print(result1)
