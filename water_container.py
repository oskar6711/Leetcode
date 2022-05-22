def max_area(height: list[int]) -> int:
    max_water = 0
    index_left = 0
    index_right = len(height) - 1

    while index_left < index_right:
        current_water = (index_right - index_left) * min(height[index_right], height[index_left])

        if current_water > max_water:
            max_water = current_water

        index_left += 1
        index_right += 1
