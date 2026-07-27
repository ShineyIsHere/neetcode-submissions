class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = numbers[0]
        right = numbers[len(numbers) - 1]
        right_shift = 0
        left_shift = 0
        while left + right != target:
            if left + right > target:
                right_shift += 1
                right = numbers[len(numbers) - 1 - right_shift]
                
            elif left + right < target:
                left_shift += 1
                left = numbers[0 + left_shift]
        return [left_shift + 1, len(numbers) - right_shift]