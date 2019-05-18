#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    """
        find the longest common prefix
        ['find', 'fire', 'five'] -> 'fi'
        ['dog', 'flow', 'car'] -> ''
    :param strs:
    :return:
    """
    if len(strs) >= 1:
        count = len(strs[0])
        if count > 0:
            for val in strs[1:]:
                if strs[0][:count] != val[:count]:
                    count -= 1
        return strs[0][:count]

    # if len(strs) >= 1:
    #     count = len(strs[0])
    #     lst_size = 1
    #     while count > 0 and lst_size < len(strs):
    #         if strs[0][:count] == strs[lst_size][:count]:
    #             lst_size += 1
    #             continue
    #         else:
    #             count -= 1
    #     return strs[0][:count]
    return ""


if __name__ == '__main__':
    print(longest_common_prefix(['dog', 'flow', 'car']))
