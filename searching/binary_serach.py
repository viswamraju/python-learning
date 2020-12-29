def search(numbers, item):
    is_exists = False
    
    lower = 0
    upper = len(numbers) - 1
    # check for lower is always less than or equal to upper
    while lower <= upper:
        # calculate mid integer division
        mid = (lower + upper) // 2
        print(f"lower: {lower}, upper: {upper}, mid: {mid}")
        
        # compare with mid position
        if numbers[mid] == item:
            return True
        else:
            # if required item is less than mid indexed value assign upper to mid -1
            if item < numbers[mid]:
                upper = mid - 1
            # if required item is greater than mid indexed value assign lower to mid + 1
            else:
                lower = mid + 1
    return is_exists


if __name__ == '__main__':
    # list should be in sorted order
    numbers = [5, 7, 8, 9, 45, 99]
    is_exists = search(numbers, 6)
    print(is_exists)
