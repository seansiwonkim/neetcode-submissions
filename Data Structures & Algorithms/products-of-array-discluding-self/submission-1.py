class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sum = 1;
        isZero = 0

        for num in nums:
            if num == 0:
                isZero += 1
            sum *= (num if num != 0 else 1)
        ans = [1] * len(nums)

        if isZero > 1:
            return [0] * len(nums)

        for i in range(len(nums)):
            if isZero == 1:
                if(nums[i] == 0):
                    ans[i] = int(sum);
                else:
                    ans[i] = 0
            else:
                ans[i] = int(sum/nums[i])
        return ans