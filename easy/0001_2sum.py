#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
        two sum
    :param nums:
    :param target:
    :return:
    """
    # Solution1: time complexity is too large
    # arr_len = len(nums)
    # for i in range(arr_len):
    #     for j in range(i+1, arr_len):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]
    # return []

    # Solution2:
    # deduplicate
    arr_len = len(nums)
    # arr_set = []
    # [arr_set.append(i) for i in nums if i not in arr_set]
    # if arr_len != len(arr_set):
    #     raise Exception("Please ensure each element in list is unique.")
    temp = {}
    for i in range(arr_len):
        minus = target - nums[i]
        if minus not in temp:
            temp[nums[i]] = i
            continue
        return [temp[minus], i]
    return []
