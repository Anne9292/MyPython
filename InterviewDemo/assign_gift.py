#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne-home
# datetime: 2021-02-21 22:03
# filename: MyPython/assign_gift

def assign_gifts(giftsIn):
    giftsOut = {}
    persons = list(giftsIn.keys())
    for p in persons:
        flag = 0
        if p in giftsIn:
            flag = 1
            myGift = giftsIn.pop(p)
        getGift = giftsIn.popitem()
        giftsOut[p] = getGift[1]
        if flag:
            giftsIn[p] = myGift
    return giftsOut


if __name__ == '__main__':
    gifts = {'anne': 'sugger', 'tony': 'apple', 'john': 'bear tony', 'william': 'book'}
    result = assign_gifts(gifts)
    print(result)
