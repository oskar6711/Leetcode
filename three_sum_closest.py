def three_sum_closest(nums: list[int], target: int) -> int:

    nums.sort()
    result = float('inf')
    print(result)

    for l in range(0, len(nums)):

        m = l + 1
        r = len(nums) - 1

        while m < r:
            total = nums[l] + nums[m] + nums[r]

            if total < target:
                m += 1

            elif total > target:
                r -= 1

            else:
                return total

            if abs(total - target) < abs(result - target):
                result = total

    return result


print(three_sum_closest([-1, 2, 1, -4], 1))