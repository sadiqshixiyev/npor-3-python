def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Находит индексы двух чисел, которые в сумме дают target.
    """
    seen = {}
    for current_index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], current_index]
        seen[num] = current_index
    return []