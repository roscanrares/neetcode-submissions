class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for _ in nums:
            if _ in dic: dic[_] += 1
            else: dic[_] = 1
        for _ in dic:
            if _ > 1: dic[_] -=1
            else: dic.pop(_)

            if (_ + _ == target) and dic[_]: return [nums.index(_), nums.index(_) + 1]
            elif (target - _) in dic: return [nums.index(_), nums.index((target - _))]
            
                
