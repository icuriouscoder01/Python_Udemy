L1 = [3, 5, 7, 9, 3, 6, 5, 2, 3, 7, 10]
res = []

for elements in L1:
    if elements not in res:
        res.append(elements)

print(f"Removed Duplicates: {res}")