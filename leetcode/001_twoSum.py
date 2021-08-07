class solution:
    def twoSum(self, nums, target):
        dict = {}
        for i, n in enumerate(nums):
            cp = target - n
            if cp in target:
                return [dict[cp], i]
            else:
                dict[n] = i