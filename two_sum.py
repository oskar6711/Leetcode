def twosum(nums, target):
    seen = {}

    for i, value in enumerate(nums):
        remaining = target - nums[i]
        print(seen)
        if remaining in seen:
            return [i, seen[remaining]]

        seen[value] = i

