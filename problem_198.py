""" Not the cleanest solution but it works

"""
from typing import List


class MWIS(object):
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.count = len(nums)
        self.costs = [None] * self.count
        self.costs[0] = self.nums[0]
        if self.nums[1] > self.nums[0]:
            self.costs[1] = self.nums[1]
        else:
            self.costs[1] = self.nums[0]

    def rec_solve(self, index: int):
        if index == 0:
            return self.costs[0]
        if index == 1:
            return self.costs[1]
        excl = index - 1
        inc = index - 2
        excl_cost = self.rec_solve(excl)
        incl_cost = self.costs[inc] + self.nums[index]
        if excl_cost > incl_cost:
            self.costs[index] = excl_cost
            return excl_cost
        else:
            self.costs[index] = incl_cost
            return incl_cost

    def get_answer(self):
        answer = self.rec_solve(self.count - 1)
        return answer


class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]
        mwis = MWIS(nums)
        return mwis.get_answer()



