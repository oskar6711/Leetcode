from collections import Counter
import bisect


def three_sum(nums):
    counter = Counter(nums)
    nums = sorted(counter)

    min_num = nums[0]
    max_num = nums[-1]

    result = []

    if 0 in counter and counter[0] >= 2:
        result.append([0, 0, 0])

    for k, v in counter.items():
        if v > 1 and k != 0 and -2 * k in counter:
            result.append([k, k, -2 * k])

    if min_num >= 0 or max_num <= 0:
        return result

    boolean = max(-min_num, max_num) / min(-min_num, max_num) > 3

    if not boolean:
        min_range_value = max(-max_num, min_num)
        max_range_value = min(-min_num, max_num)

        min_range = bisect.bisect_left(nums, min_range_value)
        max_range = bisect.bisect_right(nums, max_range_value)

    else:
        min_range = 0
        max_range = len(nums) - 1

    for i in range(len(nums) - 1):

        two_sum = -nums[i]
        min_half, max_half = two_sum - max_num, two_sum / 2

        l = bisect.bisect_left(nums, min_half, i + 1)
        r = bisect.bisect_left(nums, max_half, l)

        for j in nums[l:r]:
            if two_sum - j in counter:
                result.append([-two_sum, j, two_sum - j])

    return result
