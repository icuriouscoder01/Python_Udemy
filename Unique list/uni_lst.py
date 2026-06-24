def unique_nums(*args):
    nums = set(args)
    return list(nums)

nums = "5 7 9 2 5 7 4 3 8"
numbers = [int(n) for n in nums.split()]

unique = unique_nums(*numbers)

print("\nUnique Numbers:")
print(unique)
