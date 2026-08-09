class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for i in range(n ):
            needed = target - numbers[i]

            if needed in numbers[i + 1:]:
                return [i + 1, numbers.index(needed, i + 1) + 1]