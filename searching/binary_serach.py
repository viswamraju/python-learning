def search(numbers, item):
    is_exists = False
    
    lower = 0
    upper = len(numbers) - 1
    while lower <= upper:
        mid = (lower + upper) // 2
        print(f"lower: {lower}, upper: {upper}, mid: {mid}")
        
        if numbers[mid] == item:
            return True
        else:
            if item < numbers[mid]:
                upper = mid - 1
            else:
                lower = mid + 1
    return is_exists


if __name__ == '__main__':
    numbers = [5, 7, 8, 9, 45, 99]
    is_exists = search(numbers, 6)
    print(is_exists)
