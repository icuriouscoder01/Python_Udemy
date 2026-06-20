lst = [1, 2, 3, 4, 5, 6]
n = int(input("Enter the number you want to rotate: "))

rot = lst[n:] + lst[:n]

print(f"Rotated list: {rot}")