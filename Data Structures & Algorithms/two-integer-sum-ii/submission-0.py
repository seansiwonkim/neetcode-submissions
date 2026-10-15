class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = [0, len(numbers)-1]
        while ans[0] < ans[1]:
            if numbers[ans[0]]+numbers[ans[1]] > target:
                ans[1]-=1
            elif numbers[ans[0]]+numbers[ans[1]] < target:
                ans[0]+=1
            else:
                break
        return [ans[0]+1, ans[1]+1]