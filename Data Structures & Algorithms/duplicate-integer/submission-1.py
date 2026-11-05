class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = {}
        for _ in nums:
            if _ in check:
                return True
            check[_] = 1
        return False