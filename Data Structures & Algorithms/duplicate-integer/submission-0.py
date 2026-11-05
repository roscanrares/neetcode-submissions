class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = []
        for _ in nums:
            if _ in check:
                return True
            else:
                check.append(_)
        return False